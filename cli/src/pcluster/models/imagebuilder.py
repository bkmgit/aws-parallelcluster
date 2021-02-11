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
#
# This module contains all the classes representing the Resources objects.
# These objects are obtained from the configuration file through a conversion based on the Schema classes.
#

from typing import List

from pcluster import utils
from pcluster.models.common import BaseDevSettings, BaseTag, Resource
from pcluster.validators.ebs_validators import EBSVolumeKmsKeyIdValidator, EbsVolumeTypeSizeValidator
from pcluster.validators.ec2_validators import (
    BaseAMIValidator,
    InstanceTypeBaseAMICompatibleValidator,
    InstanceTypeValidator,
)

# ---------------------- Image ---------------------- #


class Volume(Resource):
    """Represent the volume configuration for the ImageBuilder."""

    def __init__(self, size: int = None, encrypted: bool = None, kms_key_id: str = None):
        super().__init__()
        self.size = Resource.init_param(size)
        self.encrypted = Resource.init_param(encrypted, default=False)
        self.kms_key_id = Resource.init_param(kms_key_id)
        # TODO: add validator

    def _register_validators(self):
        self._add_validator(
            EBSVolumeKmsKeyIdValidator, volume_kms_key_id=self.kms_key_id, volume_encrypted=self.encrypted
        )


class Image(Resource):
    """Represent the image configuration for the ImageBuilder."""

    def __init__(
        self,
        name: str,
        description: str = None,
        tags: List[BaseTag] = None,
        root_volume: Volume = None,
    ):
        super().__init__()
        self.name = Resource.init_param(name)
        self.description = Resource.init_param(description)
        self.tags = tags
        self.root_volume = root_volume
        self._set_default()
        # TODO: add validator

    def _set_default(self):
        if self.tags is None:
            self.tags = []
        default_tag = BaseTag("PclusterVersion", utils.get_installed_version())
        default_tag.implied = True
        self.tags.append(default_tag)


# ---------------------- Build ---------------------- #


class Component(Resource):
    """Represent the components configuration for the ImageBuilder."""

    def __init__(self, type: str = None, value: str = None):
        super().__init__()
        self.type = Resource.init_param(type)
        self.value = Resource.init_param(value)
        # TODO: add validator


class Build(Resource):
    """Represent the build configuration for the ImageBuilder."""

    def __init__(
        self,
        instance_type: str,
        parent_image: str,
        instance_role: str = None,  # TODO: auto generate if not assigned
        subnet_id: str = None,  # TODO: auto generate if not assigned
        tags: List[BaseTag] = None,
        security_group_ids: List[str] = None,
        components: List[Component] = None,
    ):
        super().__init__()
        self.instance_type = Resource.init_param(instance_type)
        self.parent_image = Resource.init_param(parent_image)
        self.instance_role = Resource.init_param(instance_role)
        self.tags = tags
        self.subnet_id = Resource.init_param(subnet_id)
        self.security_group_ids = security_group_ids
        self.components = components

    def _register_validators(self):
        self._add_validator(BaseAMIValidator, priority=15, parent_image=self.parent_image)
        self._add_validator(InstanceTypeValidator, priority=15, instance_type=self.instance_type)
        self._add_validator(
            InstanceTypeBaseAMICompatibleValidator,
            priority=14,
            instance_type=self.instance_type,
            parent_image=self.parent_image,
        )


# ---------------------- Dev Settings ---------------------- #


class ImagebuilderDevSettings(BaseDevSettings):
    """Represent the dev settings configuration for the ImageBuilder."""

    def __init__(
        self,
        update_os_and_reboot: bool = None,
        disable_pcluster_component: bool = None,
        distribution_configuration_arn: str = None,
        terminate_instance_on_failure: bool = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.update_os_and_reboot = Resource.init_param(update_os_and_reboot, default=False)
        self.disable_pcluster_component = Resource.init_param(disable_pcluster_component, default=False)
        self.distribution_configuration_arn = Resource.init_param(distribution_configuration_arn)
        self.terminate_instance_on_failure = Resource.init_param(terminate_instance_on_failure, default=True)


# ---------------------- ImageBuilder ---------------------- #


class ImageBuilder(Resource):
    """Represent the configuration of an ImageBuilder."""

    def __init__(
        self,
        image: Image,
        build: Build,
        dev_settings: ImagebuilderDevSettings = None,
    ):
        super().__init__()
        self.image = image
        self.build = build
        self.dev_settings = dev_settings
        self._set_default()

    def _register_validators(self):
        self._add_validator(
            EbsVolumeTypeSizeValidator, priority=10, volume_type="gp2", volume_size=self.image.root_volume.size
        )

    def _set_default(self):
        # set default root volume
        if self.image.root_volume is None or self.image.root_volume.size is None:
            increase_volume_size = 15
            ami_id = utils.get_ami_id(self.build.parent_image)
            ami_info = utils.get_info_for_amis([ami_id])
            default_root_volume_size = (
                ami_info[0].get("BlockDeviceMappings")[0].get("Ebs").get("VolumeSize") + increase_volume_size
            )
            if self.image.root_volume is None:
                default_root_volume = Volume(size=default_root_volume_size)
                default_root_volume.implied = True
                self.image.root_volume = default_root_volume
            else:
                self.image.root_volume.size = Resource.init_param(value=None, default=default_root_volume_size)