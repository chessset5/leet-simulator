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
    def assert_test(self, head: list, expected: list) -> None:
        """Helper to standardize sorting and assertion logic."""

        # TODO change the below to match the current Solution Object

        # pre-process
        h_node: ListNode | None = list_to_node(ls=head)  # head node
        e_node: ListNode | None = list_to_node(ls=expected)  # expected node

        # solve
        # new head
        n_head: ListNode | None = self.sol.swapPairs(head=h_node)

        # post-process

        # assert
        self.assertTrue(expr=node_is_equal(n_head, e_node))

    def test_case1(self) -> None:
        self.assert_test(head=[1, 2, 3, 4], expected=[2, 1, 4, 3])

    def test_case2(self) -> None:
        self.assert_test(head=[], expected=[])

    def test_case3(self) -> None:
        self.assert_test(head=[1, 2, 3], expected=[2, 1, 3])
