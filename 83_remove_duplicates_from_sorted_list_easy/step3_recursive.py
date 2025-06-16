#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length of list is less than 2
        if head is None or head.next is None:
            return head
        # remove head
        elif head.val == head.next.val:
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head


# @lc code=end
