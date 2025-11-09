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

        def add_two_list_nodes(
            l1: Optional[ListNode], l2: Optional[ListNode], carry_of_digits: int
        ) -> Optional[ListNode]:
            if not l1 and not l2 and carry_of_digits == 0:
                return None
            elif not l1 and not l2:
                l1 = ListNode()
                l2 = ListNode()
            elif not l1:
                l1 = ListNode()
            elif not l2:
                l2 = ListNode()

            added_list_node: ListNode = ListNode()
            carry_of_digits, digit_sum = divmod(
                l1.val + l2.val + carry_of_digits, BASE_NUMBER
            )
            added_list_node.val = digit_sum
            added_list_node.next = add_two_list_nodes(l1.next, l2.next, carry_of_digits)
            return added_list_node

        return add_two_list_nodes(l1, l2, 0)


# @lc code=end
