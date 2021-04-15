# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at http://aws.amazon.com/apache2.0/
# or in the "LICENSE.txt" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=R0801


from api import util
from api.models.base_model_ import Model


class NodeType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    HEAD = "HEAD"
    COMPUTE = "COMPUTE"

    def __init__(self):
        """NodeType - a model defined in OpenAPI"""
        self.openapi_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "NodeType":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NodeType of this NodeType.
        :rtype: NodeType
        """
        return util.deserialize_model(dikt, cls)
