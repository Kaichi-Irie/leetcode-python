#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        """
        Detect if a cycle exists and if so, where the cycle starts.
        This uses Floyd's algorithm for efficient space complexity.
        """
        if not head:
            return None
        slow_pointer = head
        fast_pointer = head
        have_cycle = False
        while fast_pointer.next and fast_pointer.next.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                have_cycle = True
                break
        if not have_cycle:
            return None

        pointer1 = head
        pointer2 = fast_pointer

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1


# @lc code=end
