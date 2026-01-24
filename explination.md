# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

This problem is just multiple link list reversals. And a check to see if the reversal is possible.

# Approach
<!-- Describe your approach to solving the problem. -->

We know we may have multiple reversed linked lists, so we will need an outer loop.

To start, we need to check if there are enough nodes to perform the K-link reversal. So we will need an inner loop to check `k` number of nodes. If we run out of nodes, we will know we can stop checking for link nodes to reverse and end both our inner and outer loop.

We can use a variable called current node, `cn`, to hold the position of the nodes we past by. We can also use `cn` in the outer loop to check if we are still reversing link nodes inside the loop. Since the outer loop will be using `cn` as a condition without knowing the advancement of the variable, a **while** loop would be best suited for the outer loop.

Since we also know the inner loops will itterate `k` times, we will give it a **for** loop

**Reversing the linked list**
As a small reminder, lets see how reversing a list in $$O(N)$$ can be done graphically.

![Screenshot 2026-01-23 at 11.53.21 PM.png](https://assets.leetcode.com/users/images/9d01f43f-1b9f-41f4-bd4b-37852d86a064_1769241216.3599935.png)

*You can try on your own to see if you can perform the above on your own code before looking at my example and explination below.*

Since we are working with a *sorted* linked lists, we only have to worry about the next node, the header node, and the tail node. Since head is already used as the input and these reversals are sub links we will refer to these as sub header and sub tail.

We can use `cn` to set the first node for the sub header and sub tail nodes.

**Steps for reversing a linked list**

1. Set the `header` and `tail` nodes. (They will start as the same node)
2. Get the next node after the `header`. We will call it `nn`.
3. Set the `header` to point to the `nn`'s next node.
4. Point the `nn` to the `tail`.
5. Set the `tail` to `nn`

Once reversed, remember to point the *last* `sub header` to the *current* `sub tail`. Then store the *current* `sub header` into *last* for the *next* `sub tail`.

Continue until you have reached the end of the list. IE `cn` is a `null` value.

***Note**: For my code below, the act of checking the nodes before the reversal advances the `cn` value.*

# Complexity

- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(N)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

# Code

```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cn: Optional[ListNode] = head  # current node
        head = None
        ln: Optional[ListNode] = None
        while cn is not None:
            # set the sub ends before counting the nodes
            shn: Optional[ListNode] = cn  # sub head node
            stn: Optional[ListNode] = cn  # sub tail node

            # verify there are enough nodes left
            cnt: int = 0
            for i in range(k):
                if cn is None:
                    break
                cn = cn.next
                cnt += 1
            if cnt < k:
                break

            # k-reverse linked list
            # k-1 because each time we loop we affect two nodes.
            for i in range(k-1):
                # store next node
                nn: Optional[ListNode] = shn.next  # next node

                # point sub header to nn.next
                shn.next = nn.next

                # put nn.next to stn
                nn.next = stn

                # update tail to nn
                stn = nn

            if head is None:
                # set the first sub tail node to the new head
                # set the last node
                head = stn
                ln = shn
            else:
                # point the head of the last reverse list 
                # to the tail of the current, then update
                # the "last" head.
                ln.next = stn
                ln = shn

        return head

```
