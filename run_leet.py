"""
single runner for leet, use for debugging
"""

from leet import Solution
from LeetTypes.single_list_node import ListNode, list_to_node, node_to_list

# add input below

s = Solution()

head: ListNode | None = list_to_node(ls=[1, 2, 3, 4, 5])

head = s.reverseKGroup(head=head, k=2)

print(node_to_list(head=head))
