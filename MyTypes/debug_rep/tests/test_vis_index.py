"""
Unit tests for leet
"""

# pylint: disable=W0611

import unittest
from typing import Any, List, Optional

from MyTypes.debug_rep.vis_index import StrIndex, BinIntIndex

# pylint: disable=C0115
# pylint: disable=C0116


class StrIndexTesting(unittest.TestCase):
    """
    unit test class for Solution
    """

    # pylint: disable=W0511
    def assert_repr_test(self, string: str, index: int, expected: str) -> None:
        """Helper to standardize sorting and assertion logic."""

        output: Any = repr(StrIndex(string, index))

        # assert
        self.assertEqual(output, expected)

    def test_overflow(self) -> None:
        self.assert_repr_test(string="apples", index=8, expected="ap[p]les")


class BinIntIndexTesting(unittest.TestCase):
    """
    unit test class for Solution
    """

    # pylint: disable=W0511
    def assert_repr_test(self, integer: int, index: int, expected: str) -> None:
        """Helper to standardize sorting and assertion logic."""

        output: Any = repr(BinIntIndex(integer, index))

        # assert
        self.assertEqual(output, expected)

    def test_overflow(self) -> None:
        with self.assertRaises(expected_exception=IndexError):
            BinIntIndex(5, 8)
