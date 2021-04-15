# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


from datetime import datetime
from typing import List

from api import util
from api.models.base_model_ import Model
from api.models.cloud_formation_status import CloudFormationStatus
from api.models.ec2_ami_info import Ec2AmiInfo
from api.models.image_build_status import ImageBuildStatus
from api.models.image_builder_image_status import ImageBuilderImageStatus
from api.models.image_configuration_structure import ImageConfigurationStructure
from api.models.tag import Tag


class DescribeImageResponseContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(
        self,
        image_configuration=None,
        image_name=None,
        imagebuilder_image_status=None,
        creation_time=None,
        image_build_status=None,
        failure_reason=None,
        cloudformation_stack_status=None,
        cloudformation_stack_arn=None,
        region=None,
        ec2_ami_info=None,
        version=None,
        tags=None,
    ):
        """DescribeImageResponseContent - a model defined in OpenAPI

        :param image_configuration: The image_configuration of this DescribeImageResponseContent.
        :type image_configuration: ImageConfigurationStructure
        :param image_name: The image_name of this DescribeImageResponseContent.
        :type image_name: str
        :param imagebuilder_image_status: The imagebuilder_image_status of this DescribeImageResponseContent.
        :type imagebuilder_image_status: ImageBuilderImageStatus
        :param creation_time: The creation_time of this DescribeImageResponseContent.
        :type creation_time: datetime
        :param image_build_status: The image_build_status of this DescribeImageResponseContent.
        :type image_build_status: ImageBuildStatus
        :param failure_reason: The failure_reason of this DescribeImageResponseContent.
        :type failure_reason: str
        :param cloudformation_stack_status: The cloudformation_stack_status of this DescribeImageResponseContent.
        :type cloudformation_stack_status: CloudFormationStatus
        :param cloudformation_stack_arn: The cloudformation_stack_arn of this DescribeImageResponseContent.
        :type cloudformation_stack_arn: str
        :param region: The region of this DescribeImageResponseContent.
        :type region: str
        :param ec2_ami_info: The ec2_ami_info of this DescribeImageResponseContent.
        :type ec2_ami_info: Ec2AmiInfo
        :param version: The version of this DescribeImageResponseContent.
        :type version: str
        :param tags: The tags of this DescribeImageResponseContent.
        :type tags: List[Tag]
        """
        self.openapi_types = {
            "image_configuration": ImageConfigurationStructure,
            "image_name": str,
            "imagebuilder_image_status": ImageBuilderImageStatus,
            "creation_time": datetime,
            "image_build_status": ImageBuildStatus,
            "failure_reason": str,
            "cloudformation_stack_status": CloudFormationStatus,
            "cloudformation_stack_arn": str,
            "region": str,
            "ec2_ami_info": Ec2AmiInfo,
            "version": str,
            "tags": List[Tag],
        }

        self.attribute_map = {
            "image_configuration": "imageConfiguration",
            "image_name": "imageName",
            "imagebuilder_image_status": "imagebuilderImageStatus",
            "creation_time": "creationTime",
            "image_build_status": "imageBuildStatus",
            "failure_reason": "failureReason",
            "cloudformation_stack_status": "cloudformationStackStatus",
            "cloudformation_stack_arn": "cloudformationStackArn",
            "region": "region",
            "ec2_ami_info": "ec2AmiInfo",
            "version": "version",
            "tags": "tags",
        }

        self._image_configuration = image_configuration
        self._image_name = image_name
        self._imagebuilder_image_status = imagebuilder_image_status
        self._creation_time = creation_time
        self._image_build_status = image_build_status
        self._failure_reason = failure_reason
        self._cloudformation_stack_status = cloudformation_stack_status
        self._cloudformation_stack_arn = cloudformation_stack_arn
        self._region = region
        self._ec2_ami_info = ec2_ami_info
        self._version = version
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt) -> "DescribeImageResponseContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DescribeImageResponseContent of this DescribeImageResponseContent.
        :rtype: DescribeImageResponseContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_configuration(self):
        """Gets the image_configuration of this DescribeImageResponseContent.


        :return: The image_configuration of this DescribeImageResponseContent.
        :rtype: ImageConfigurationStructure
        """
        return self._image_configuration

    @image_configuration.setter
    def image_configuration(self, image_configuration):
        """Sets the image_configuration of this DescribeImageResponseContent.


        :param image_configuration: The image_configuration of this DescribeImageResponseContent.
        :type image_configuration: ImageConfigurationStructure
        """
        if image_configuration is None:
            raise ValueError("Invalid value for `image_configuration`, must not be `None`")

        self._image_configuration = image_configuration

    @property
    def image_name(self):
        """Gets the image_name of this DescribeImageResponseContent.

        Name of the Image

        :return: The image_name of this DescribeImageResponseContent.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this DescribeImageResponseContent.

        Name of the Image

        :param image_name: The image_name of this DescribeImageResponseContent.
        :type image_name: str
        """
        if image_name is None:
            raise ValueError("Invalid value for `image_name`, must not be `None`")

        self._image_name = image_name

    @property
    def imagebuilder_image_status(self):
        """Gets the imagebuilder_image_status of this DescribeImageResponseContent.


        :return: The imagebuilder_image_status of this DescribeImageResponseContent.
        :rtype: ImageBuilderImageStatus
        """
        return self._imagebuilder_image_status

    @imagebuilder_image_status.setter
    def imagebuilder_image_status(self, imagebuilder_image_status):
        """Sets the imagebuilder_image_status of this DescribeImageResponseContent.


        :param imagebuilder_image_status: The imagebuilder_image_status of this DescribeImageResponseContent.
        :type imagebuilder_image_status: ImageBuilderImageStatus
        """

        self._imagebuilder_image_status = imagebuilder_image_status

    @property
    def creation_time(self):
        """Gets the creation_time of this DescribeImageResponseContent.

        Timestamp representing the image creation time

        :return: The creation_time of this DescribeImageResponseContent.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DescribeImageResponseContent.

        Timestamp representing the image creation time

        :param creation_time: The creation_time of this DescribeImageResponseContent.
        :type creation_time: datetime
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")

        self._creation_time = creation_time

    @property
    def image_build_status(self):
        """Gets the image_build_status of this DescribeImageResponseContent.


        :return: The image_build_status of this DescribeImageResponseContent.
        :rtype: ImageBuildStatus
        """
        return self._image_build_status

    @image_build_status.setter
    def image_build_status(self, image_build_status):
        """Sets the image_build_status of this DescribeImageResponseContent.


        :param image_build_status: The image_build_status of this DescribeImageResponseContent.
        :type image_build_status: ImageBuildStatus
        """
        if image_build_status is None:
            raise ValueError("Invalid value for `image_build_status`, must not be `None`")

        self._image_build_status = image_build_status

    @property
    def failure_reason(self):
        """Gets the failure_reason of this DescribeImageResponseContent.

        Describe the reason of the failure when the stack is in CREATE_FAILED, UPDATE_FAILED or DELETE_FAILED status

        :return: The failure_reason of this DescribeImageResponseContent.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this DescribeImageResponseContent.

        Describe the reason of the failure when the stack is in CREATE_FAILED, UPDATE_FAILED or DELETE_FAILED status

        :param failure_reason: The failure_reason of this DescribeImageResponseContent.
        :type failure_reason: str
        """

        self._failure_reason = failure_reason

    @property
    def cloudformation_stack_status(self):
        """Gets the cloudformation_stack_status of this DescribeImageResponseContent.


        :return: The cloudformation_stack_status of this DescribeImageResponseContent.
        :rtype: CloudFormationStatus
        """
        return self._cloudformation_stack_status

    @cloudformation_stack_status.setter
    def cloudformation_stack_status(self, cloudformation_stack_status):
        """Sets the cloudformation_stack_status of this DescribeImageResponseContent.


        :param cloudformation_stack_status: The cloudformation_stack_status of this DescribeImageResponseContent.
        :type cloudformation_stack_status: CloudFormationStatus
        """
        if cloudformation_stack_status is None:
            raise ValueError("Invalid value for `cloudformation_stack_status`, must not be `None`")

        self._cloudformation_stack_status = cloudformation_stack_status

    @property
    def cloudformation_stack_arn(self):
        """Gets the cloudformation_stack_arn of this DescribeImageResponseContent.

        ARN of the main CloudFormation stack

        :return: The cloudformation_stack_arn of this DescribeImageResponseContent.
        :rtype: str
        """
        return self._cloudformation_stack_arn

    @cloudformation_stack_arn.setter
    def cloudformation_stack_arn(self, cloudformation_stack_arn):
        """Sets the cloudformation_stack_arn of this DescribeImageResponseContent.

        ARN of the main CloudFormation stack

        :param cloudformation_stack_arn: The cloudformation_stack_arn of this DescribeImageResponseContent.
        :type cloudformation_stack_arn: str
        """
        if cloudformation_stack_arn is None:
            raise ValueError("Invalid value for `cloudformation_stack_arn`, must not be `None`")

        self._cloudformation_stack_arn = cloudformation_stack_arn

    @property
    def region(self):
        """Gets the region of this DescribeImageResponseContent.

        AWS region where the image is created

        :return: The region of this DescribeImageResponseContent.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DescribeImageResponseContent.

        AWS region where the image is created

        :param region: The region of this DescribeImageResponseContent.
        :type region: str
        """
        if region is None:
            raise ValueError("Invalid value for `region`, must not be `None`")

        self._region = region

    @property
    def ec2_ami_info(self):
        """Gets the ec2_ami_info of this DescribeImageResponseContent.


        :return: The ec2_ami_info of this DescribeImageResponseContent.
        :rtype: Ec2AmiInfo
        """
        return self._ec2_ami_info

    @ec2_ami_info.setter
    def ec2_ami_info(self, ec2_ami_info):
        """Sets the ec2_ami_info of this DescribeImageResponseContent.


        :param ec2_ami_info: The ec2_ami_info of this DescribeImageResponseContent.
        :type ec2_ami_info: Ec2AmiInfo
        """

        self._ec2_ami_info = ec2_ami_info

    @property
    def version(self):
        """Gets the version of this DescribeImageResponseContent.

        ParallelCluster version used to build the image

        :return: The version of this DescribeImageResponseContent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DescribeImageResponseContent.

        ParallelCluster version used to build the image

        :param version: The version of this DescribeImageResponseContent.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version

    @property
    def tags(self):
        """Gets the tags of this DescribeImageResponseContent.

        Tags of the infrastructure to build the Image

        :return: The tags of this DescribeImageResponseContent.
        :rtype: List[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DescribeImageResponseContent.

        Tags of the infrastructure to build the Image

        :param tags: The tags of this DescribeImageResponseContent.
        :type tags: List[Tag]
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")

        self._tags = tags
