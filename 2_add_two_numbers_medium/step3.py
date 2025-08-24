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

BASE_NUMBER = 10


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # to save head node, we preapare head_dummy
        head_dummy = ListNode()

        node: ListNode = head_dummy
        carry_of_digits = 0

        # visit each node iteratively and create added digit one by one
        # break the loop if two nodes l1 and l2 are None and no carry of digits
        while l1 or l2 or carry_of_digits:
            # add two nodes
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry_of_digits
            carry_of_digits, digit = divmod(total, BASE_NUMBER)
            node.next = ListNode(digit)

            # move to next node
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head_dummy.next


# @lc code=end
