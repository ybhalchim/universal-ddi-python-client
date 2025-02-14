# coding: utf-8

"""
    IPAM Federation API

    The DDI IPAM Federation application enables a SaaS administrator to manage multiple IPAM systems from one central control point CSP.    

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from ipam_federation.api.next_available_overlapping_block_api import NextAvailableOverlappingBlockApi

from universal_ddi_client.api_client import ApiClient


class TestNextAvailableOverlappingBlockApi(unittest.TestCase):
    """NextAvailableOverlappingBlockApi unit test stubs"""

    def setUp(self) -> None:
        api_instance = ApiClient()
        self.api = NextAvailableOverlappingBlockApi(api_instance)

    def tearDown(self) -> None:
        pass

    def test_list_next_available_overlapping_blocks(self) -> None:
        """Test case for list_next_available_overlapping_blocks

        List the next available overlapping block.
        """
        pass


if __name__ == '__main__':
    unittest.main()
