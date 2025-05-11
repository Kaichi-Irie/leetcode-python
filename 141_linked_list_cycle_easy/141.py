from typing import Optional

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        if slow.next is None:
            return False
        while True:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


# @lc code=end
