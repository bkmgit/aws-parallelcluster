"""
    ParallelCluster

    ParallelCluster API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pcluster.api.client
from pcluster.api.client.model.instance_state import InstanceState
from pcluster.api.client.model.node_type import NodeType
globals()['InstanceState'] = InstanceState
globals()['NodeType'] = NodeType
from pcluster.api.client.model.cluster_instance import ClusterInstance


class TestClusterInstance(unittest.TestCase):
    """ClusterInstance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterInstance(self):
        """Test ClusterInstance"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterInstance()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()