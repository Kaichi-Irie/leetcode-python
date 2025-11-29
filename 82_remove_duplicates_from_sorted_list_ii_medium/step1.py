#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode|None) -> ListNode|None:
        node = head
        head = previous_node = ListNode(next=head)

        while node and node.next:
            # no duplicates
            if node.val != node.next.val:
                previous_node = node
                node = node.next
                continue

            # deduplicate
            while node and node.next and node.val == node.next.val:
                node.next = node.next.next
            previous_node.next = node.next
            node = node.next

        return head.next



# @lc code=end
