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
from api.models.cluster_info_summary import ClusterInfoSummary


class DeleteClusterResponseContent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cluster=None):
        """DeleteClusterResponseContent - a model defined in OpenAPI

        :param cluster: The cluster of this DeleteClusterResponseContent.
        :type cluster: ClusterInfoSummary
        """
        self.openapi_types = {"cluster": ClusterInfoSummary}

        self.attribute_map = {"cluster": "cluster"}

        self._cluster = cluster

    @classmethod
    def from_dict(cls, dikt) -> "DeleteClusterResponseContent":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeleteClusterResponseContent of this DeleteClusterResponseContent.
        :rtype: DeleteClusterResponseContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cluster(self):
        """Gets the cluster of this DeleteClusterResponseContent.


        :return: The cluster of this DeleteClusterResponseContent.
        :rtype: ClusterInfoSummary
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this DeleteClusterResponseContent.


        :param cluster: The cluster of this DeleteClusterResponseContent.
        :type cluster: ClusterInfoSummary
        """
        if cluster is None:
            raise ValueError("Invalid value for `cluster`, must not be `None`")

        self._cluster = cluster
