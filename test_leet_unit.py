"""
Unit tests for leet
"""

# pylint: disable=W0611

import unittest
from typing import Any, List, Optional

from leet import Solution
from LeetTypes.single_list_node import ListNode, list_to_node, node_is_equal

# pylint: disable=C0115
# pylint: disable=C0116


class SolutionTesting(unittest.TestCase):
    """
    unit test class for Solution
    """

    def setUp(self):
        """Initialize the solution once for all tests."""
        self.sol = Solution()

    # pylint: disable=W0511
    # TODO change to match current Solution Object
    def assert_test(self, dividend: int, divisor: int, expected: int) -> None:
        """Helper to standardize sorting and assertion logic."""

        # TODO change the below to match the current Solution Object

        # pre-process

        # solve
        # index
        output: Any = self.sol.divide(dividend, divisor)

        # post-process

        # assert
        self.assertEqual(output, expected)

    def test_case1(self) -> None:
        self.assert_test(dividend=10, divisor=3, expected=3)

    def test_case2(self) -> None:
        self.assert_test(dividend=7, divisor=-3, expected=-2)

    def test_case3(self) -> None:
        self.assert_test(dividend=-2147483648, divisor=-1, expected=2147483648)
