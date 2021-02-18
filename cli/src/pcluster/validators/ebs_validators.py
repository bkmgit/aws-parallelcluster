# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.
import boto3
from botocore.exceptions import ClientError

from pcluster.config.validators import (
    EBS_VOLUME_IOPS_BOUNDS,
    EBS_VOLUME_TYPE_TO_IOPS_RATIO,
    EBS_VOLUME_TYPE_TO_VOLUME_SIZE_BOUNDS,
)
from pcluster.utils import get_ebs_snapshot_info, get_partition
from pcluster.validators.common import FailureLevel, Validator


class EbsVolumeTypeSizeValidator(Validator):
    """EBS volume type and size validator.

    Validate that the EBS volume size matches the chosen volume type.

    The default value of volume_size for EBS volumes is 20 GiB.
    The volume size of standard ranges from 1 GiB - 1 TiB(1024 GiB)
    The volume size of gp2 and gp3 ranges from 1 GiB - 16 TiB(16384 GiB)
    The volume size of io1 and io2 ranges from 4 GiB - 16 TiB(16384 GiB)
    The volume sizes of st1 and sc1 range from 500 GiB - 16 TiB(16384 GiB)
    """

    def _validate(self, volume_type: str, volume_size: int):
        if volume_type in EBS_VOLUME_TYPE_TO_VOLUME_SIZE_BOUNDS:
            min_size, max_size = EBS_VOLUME_TYPE_TO_VOLUME_SIZE_BOUNDS.get(volume_type)
            if volume_size > max_size:
                self._add_failure(
                    "The size of {0} volumes can not exceed {1} GiB".format(volume_type, max_size),
                    FailureLevel.ERROR,
                )
            elif volume_size < min_size:
                self._add_failure(
                    "The size of {0} volumes must be at least {1} GiB".format(volume_type, min_size),
                    FailureLevel.ERROR,
                )


class EbsVolumeThroughputValidator(Validator):
    """
    EBS volume throughput validator.

    Validate gp3 throughput.
    """

    def _validate(self, volume_type, volume_throughput):
        if volume_type == "gp3":
            min_throughput, max_throughput = 125, 1000
            if volume_throughput < min_throughput or volume_throughput > max_throughput:
                self._add_failure(
                    "Throughput must be between {min_throughput} MB/s and {max_throughput} MB/s when provisioning "
                    "{volume_type} volumes.".format(
                        min_throughput=min_throughput, max_throughput=max_throughput, volume_type=volume_type
                    ),
                    FailureLevel.ERROR,
                )


class EbsVolumeThroughputIopsValidator(Validator):
    """
    EBS volume throughput to iops ratio validator.

    Validate gp3 throughput.
    """

    def _validate(self, volume_type, volume_iops, volume_throughput):
        volume_throughput_to_iops_ratio = 0.25
        if volume_type == "gp3":
            if volume_throughput and volume_throughput > volume_iops * volume_throughput_to_iops_ratio:
                self._add_failure(
                    "Throughput to IOPS ratio of {0} is too high; maximum is 0.25.".format(
                        float(volume_throughput) / float(volume_iops)
                    ),
                    FailureLevel.ERROR,
                )


class EbsVolumeIopsValidator(Validator):
    """
    EBS volume IOPS validator.

    Validate IOPS value in respect of volume type.
    """

    def _validate(self, volume_type, volume_size, volume_iops):
        if volume_type in EBS_VOLUME_IOPS_BOUNDS:
            min_iops, max_iops = EBS_VOLUME_IOPS_BOUNDS.get(volume_type)
            if volume_iops and (volume_iops < min_iops or volume_iops > max_iops):
                self._add_failure(
                    f"IOPS rate must be between {min_iops} and {max_iops}" f" when provisioning {volume_type} volumes.",
                    FailureLevel.ERROR,
                )
            elif volume_iops and volume_iops > volume_size * EBS_VOLUME_TYPE_TO_IOPS_RATIO[volume_type]:
                self._add_failure(
                    "IOPS to volume size ratio of {0} is too high; maximum is {1}.".format(
                        float(volume_iops) / float(volume_size),
                        EBS_VOLUME_TYPE_TO_IOPS_RATIO[volume_type],
                    ),
                    FailureLevel.ERROR,
                )


class EbsVolumeSizeSnapshotValidator(Validator):
    """
    EBS volume size snapshot validator.

    Validate the following cases:
    - The EBS snapshot is in "completed" state if it is specified.
    - If users specify the volume size, the volume must be not smaller than the volume size of the EBS snapshot.
    """

    def _validate(self, snapshot_id: int, volume_size: int):
        if snapshot_id:
            try:
                snapshot_response_dict = get_ebs_snapshot_info(snapshot_id, raise_exceptions=True)

                # validate that the input volume size is larger than the volume size of the EBS snapshot
                snapshot_volume_size = snapshot_response_dict.get("VolumeSize")
                if snapshot_volume_size is None:
                    self._add_failure(f"Unable to get volume size for snapshot {snapshot_id}", FailureLevel.ERROR)
                elif volume_size < snapshot_volume_size:
                    self._add_failure(
                        f"The EBS volume size must not be smaller than {snapshot_volume_size}, "
                        "because it is the size of the provided snapshot {snapshot_id}",
                        FailureLevel.ERROR,
                    )
                elif volume_size > snapshot_volume_size:
                    self._add_failure(
                        "The specified volume size is larger than snapshot size. In order to use the full capacity "
                        "of the volume, you'll need to manually resize the partition according to this doc: "
                        "https://{partition_url}/AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.html".format(
                            partition_url="docs.amazonaws.cn" if get_partition() == "aws-cn" else "docs.aws.amazon.com"
                        ),
                        FailureLevel.WARNING,
                    )

                # validate that the state of ebs snapshot
                if snapshot_response_dict.get("State") != "completed":
                    self._add_failure(
                        "Snapshot {0} is in state '{1}' not 'completed'".format(
                            snapshot_id, snapshot_response_dict.get("State")
                        ),
                        FailureLevel.WARNING,
                    )
            except Exception as exception:
                if isinstance(exception, ClientError) and exception.response.get("Error").get("Code") in [
                    "InvalidSnapshot.NotFound",
                    "InvalidSnapshot.Malformed",
                ]:
                    self._add_failure(
                        "The snapshot {0} does not appear to exist: {1}".format(
                            snapshot_id, exception.response.get("Error").get("Message")
                        ),
                        FailureLevel.ERROR,
                    )
                else:
                    self._add_failure(
                        "Issue getting info for snapshot {0}: {1}".format(
                            snapshot_id,
                            exception.response.get("Error").get("Message")
                            if isinstance(exception, ClientError)
                            else exception,
                        ),
                        FailureLevel.ERROR,
                    )


class EBSVolumeKmsKeyIdValidator(Validator):
    """
    EBS volume KmsKeyId validator.

    Validate KmsKeyId value based on encrypted value.
    """

    def _validate(self, volume_kms_key_id, volume_encrypted):
        if volume_kms_key_id and not volume_encrypted:
            self._add_failure(
                "Kms Key Id {0} is specified, the encrypted state must be True.".format(volume_kms_key_id),
                FailureLevel.ERROR,
            )


class SharedEBSVolumeIdValidator(Validator):
    """
    SharedEBS volume id validator.

    Validate the volume exist and is available.
    """

    def _validate(self, volume_id: str):
        if volume_id:
            try:
                respond = boto3.client("ec2").describe_volumes(VolumeIds=[volume_id]).get("Volumes")[0]
                if respond.get("State") != "available":
                    self._add_failure(
                        "Volume {0} is in state '{1}' not 'available'".format(volume_id, respond.get("State")),
                        FailureLevel.WARNING,
                    )
            except ClientError as e:
                if (
                    e.response.get("Error")
                    .get("Message")
                    .endswith("parameter volumes is invalid. Expected: 'vol-...'.")
                ):
                    self._add_failure("Volume {0} does not exist".format(volume_id), FailureLevel.ERROR)
                else:
                    self._add_failure(e.response.get("Error").get("Message"), FailureLevel.ERROR)