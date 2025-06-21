#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional

# we consider addition in base 10
BASE_NUMBER = 10


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        addTwoNumbers iteratively creates nodes and set added value to each of them.
        Created linked list look like this; dummy_head -> node0 -> node1 ->... -> last_node
        return value is dummy_head.next (=node0)
        """
        # save dummy head for returning head node
        dummy_head: ListNode = ListNode()

        # initialize first node and carry of digits
        node = dummy_head
        carry_of_digits = 0
        while l1 or l2 or carry_of_digits:
            # add two values and carry_of_digits
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry_of_digits
            carry_of_digits, digit = divmod(total, BASE_NUMBER)
            node.next = ListNode(digit)

            # move to next node
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next


# @lc code=end
