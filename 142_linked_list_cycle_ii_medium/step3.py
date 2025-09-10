#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = w
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None
        seen_nodes = set()
        node = head
        while node:
            if node in seen_nodes:
                return node
            seen_nodes.add(node)
            node = node.next
        return None


# @lc code=end
