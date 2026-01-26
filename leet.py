"""
Problem

28. Find the Index of the First Occurrence in a String

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

from typing import Optional

from LeetTypes.single_list_node import ListNode, node_to_list, repr_node

from MyTypes.debug_rep.strIndex import strIndex


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i: int = 0  # index
        j: int = 0  # jndex
        setback: int = 0  # setback for duplicate character to 0 index, eg: issi
        while i < len(haystack):
            if (len(haystack) - i) < len(needle):
                return -1
            while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                if setback == 0 and j > 0 and haystack[i] == needle[0]:
                    setback = i
                i += 1
                j += 1
            if j == len(needle) and haystack[i - 1] == needle[j - 1]:
                # if needle found
                # cur pos, minus len of needle
                return i - len(needle)
            else:
                # set back to previous, double advance i, reset j
                if setback:
                    i = setback
                    setback = 0
                elif not j:
                    i += 1
                j = 0
        return -1
