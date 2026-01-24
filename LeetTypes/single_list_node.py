"""
Docstring for LeetTypes.singleListNode

file for the ListNode class from leetcode and helper functions to help
test the Solution
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """
    singly-linked list class defined by LeetCode
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_node(ls: list) -> Optional[ListNode]:
    """
    Helper function for the ListNode object.

    :param ls: list to turn into a singly-linked ListNode
    :type ls: list
    :return: ListNode chain or None
    :rtype: ListNode | None
    """
    head: ListNode | None = None
    cn: ListNode | None = None
    for i in ls:
        if cn is None:
            cn = ListNode(i)
            head = cn
        else:
            cn.next = ListNode(i)
            cn = cn.next

    return head


def node_to_list(head: Optional[ListNode]) -> list:
    """
    Turns a Node into a List

    :param head: head node to turn into a list
    :type head: Optional[ListNode]
    :return: list of head node
    :rtype: list[Any]
    """
    ls: list = []
    while head is not None:
        ls.append(head.val)
        head = head.next
    return ls


def node_is_equal(lhs: Optional[ListNode], rhs: Optional[ListNode]) -> bool:
    """
    compares single list nodes

    :param lhs: left node list
    :type lhs: Optional[ListNode]
    :param rhs: right node list
    :type rhs: Optional[ListNode]
    :return: Description
    :rtype: bool
    """
    while lhs is not None and rhs is not None:
        if lhs.val == rhs.val:
            lhs = lhs.next
            rhs = rhs.next
        else:
            return False
    return lhs is None and rhs is None
