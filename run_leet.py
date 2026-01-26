"""
single runner for leet, use for debugging
"""

from leet import Solution
from LeetTypes.single_list_node import ListNode, list_to_node, node_to_list

# add input below

s = Solution()


index: int = s.strStr(haystack="sadbutsad", needle="sad")

print(index)
