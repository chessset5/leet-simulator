"""
Problem

24. Swap Nodes in Pairs

<https://leetcode.com/problems/swap-nodes-in-pairs/description/>

"""

from typing import Optional

from LeetTypes.single_list_node import ListNode, node_to_list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        if head.next is None:
            return head

        cn: ListNode | None = head  # current node
        head = None
        ln: ListNode | None = head  # last node
        while cn is not None:
            fp: ListNode | None = cn  # first possition
            sp: ListNode | None = fp.next  # second possition

            # break away early if second is None
            if sp is None:
                break

            if ln is not None:
                ln.next = sp

            # swap possitions
            fp.next = sp.next
            sp.next = fp

            ln = fp

            # set new head if not set
            if head is None:
                head = sp

            # advance pointer
            cn = fp.next

        return head
