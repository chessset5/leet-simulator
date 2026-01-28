"""
Problem

`29. Divide Two Integers`

<https://leetcode.com/problems/divide-two-integers/>

Given two integers dividend and divisor,
divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero,
which means losing its fractional part. For example,
8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers
within the 32-bit signed integer range: [−231, 231 − 1]. For this problem,
if the quotient is strictly greater than 231 - 1, then return 231 - 1,
and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0

"""

# pylint: disable=W0611

from typing import Optional

from LeetTypes.single_list_node import ListNode, node_to_list, repr_node

from MyTypes.debug_rep.strIndex import strIndex

# pylint: disable=C0115
# pylint: disable=C0116

# NOTE: I based this off the divisor wiki page,
#  https://en.wikipedia.org/wiki/Division_algorithm


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # no need to check for 0
        # make the inputs positive
        if divisor < 0:
            output: int = self.divide(dividend, -divisor)
            return -output  # negate input
        if dividend < 0:
            output: int = self.divide(-dividend, divisor)
            return -output  # negate input
        # Note, if both inputs are negative,
        # since the output is negated twice, it becomes positive again

        # implementing the divisor algorithm

        quotent: int = 0
        remainder: int = 0
        index: int = len(bin(dividend)) - 1 - 2
        # bin returns a bstring '0bx', where x is the bits of the string
        # so we subtract 2 extra chars
        while index >= 0:
            remainder <<= 1
            bit = int(bool(dividend & (1 << (index - 2))))  # Note this might have to shift by +-2
            remainder |= bit << 0
            if remainder >= divisor:
                remainder -= divisor
                dividend |= 1 << index
            index -= 1
        return quotent
