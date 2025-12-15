#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node|None' = None, random: 'Node|None' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node|None') -> 'Node|None':
        if head is None:
            return None
        original_to_copy = {None:None}
        copy_head = Node(head.val)
        node = head
        copy_node = copy_head
        original_to_copy[node] = copy_node
        while node.next is not None:
            copy_node.next = Node(node.next.val)
            original_to_copy[node.next] = copy_node.next
            node = node.next
            copy_node = copy_node.next
        node = head
        copy_node = copy_head
        while node is not None:
            copy_node.random = original_to_copy[node.random]
            node = node.next
            copy_node = copy_node.next

        return copy_head

# @lc code=end
