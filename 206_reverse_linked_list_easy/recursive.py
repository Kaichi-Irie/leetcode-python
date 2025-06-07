#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse_list_recursive(
            self, head: Optional[ListNode]
        ) -> Optional[ListNode]:

            if head is None or head.next is None:
                return head
            
            next_node = head.next
            reversed_nodes = reverse_list_recursive(self, next_node)
            next_node.next = head
            head.next = None
            return reversed_nodes

        return reverse_list_recursive(self, head)


# @lc code=end
