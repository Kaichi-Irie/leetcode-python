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
        original_to_copy = {}
        def get_copied_node(node: Node|None) -> Node|None:
            if node is None:
                return None
            if node in original_to_copy:
                return original_to_copy[node]
            new_node = Node(node.val)
            original_to_copy[node] = new_node
            return new_node

        node = head
        copied_node = get_copied_node(head)
        while node is not None:
            copied_node.next = get_copied_node(node.next)
            copied_node.random = get_copied_node(node.random)
            node = node.next
            copied_node = copied_node.next
        return get_copied_node(head)

# @lc code=end
