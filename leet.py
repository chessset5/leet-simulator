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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cn: Optional[ListNode] = head  # current node
        head = None
        while cn is not None:
            stn: Optional[ListNode] = cn  # sub tail node
            shn: Optional[ListNode] = cn  # sub head node

            # verify there are enough nodes left
            cnt: int = 0
            for i in range(k):
                if cn is None:
                    break
                cn = cn.next
                cnt += 1
            if cnt < k:
                break

            for i in range(k):
                # store next node
                nn: Optional[ListNode] = shn.next  # next node

                # point sub header to nn.next
                shn.next = nn.next

                # put nn.next to stn
                nn.next = stn

                # update tail to nn
                stn = nn

            # set the first sub tail node to the new head
            if head is None:
                head = stn

            # update the current node
            cn = cn.next

        return head
