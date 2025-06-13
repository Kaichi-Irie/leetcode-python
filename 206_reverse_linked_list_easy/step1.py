#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Case of where number of nodes is <= 1
        if head is None or head.next is None:
            return head


        previous = head
        current = head.next
        head.next = None

        while current.next:
            next = current.next
            current.next = previous
            previous = current
            current = next

        current.next = previous
        return current


# @lc code=end
