"""
Unit tests for leet
"""

import unittest
from typing import List, Optional

from leet import Solution
from LeetTypes.single_list_node import ListNode, list_to_node, node_is_equal


class SolutionTesting(unittest.TestCase):
    """
    unit test class for Solution
    """

    def setUp(self):
        """Initialize the solution once for all tests."""
        self.sol = Solution()

    # TODO change to match current Solution Object
    def assert_test(self, haystack: str, needle: str, expected: int) -> None:
        """Helper to standardize sorting and assertion logic."""

        # TODO change the below to match the current Solution Object

        # pre-process

        # solve
        # index
        index: int = self.sol.strStr(haystack=haystack, needle=needle)

        # post-process

        # assert
        self.assertTrue(expr=index == expected)

    def test_case1(self) -> None:
        self.assert_test(haystack="sadbutsad", needle="sad", expected=0)

    def test_case2(self) -> None:
        self.assert_test(haystack="leetcode", needle="leeto", expected=-1)
