"""
single runner for leet, use for debugging
"""

from leet import Solution
from LeetTypes.single_list_node import ListNode, list_to_node

# add input below

s = Solution()

head: ListNode | None = list_to_node([1, 2, 3, 4])

head = s.swapPairs(head=head)
