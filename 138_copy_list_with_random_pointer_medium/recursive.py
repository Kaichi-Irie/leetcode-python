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
    def __init__(self):
        self.original_to_copy = {None:None}
    def copyRandomList(self, head: 'Node|None') -> 'Node|None':
        if head is None:
            return None
        if head in self.original_to_copy:
            return self.original_to_copy[head]
        copy_head = Node(head.val)
        self.original_to_copy[head] = copy_head
        copy_head.next = self.copyRandomList(head.next)
        copy_head.random = self.copyRandomList(head.random)

        return copy_head

# @lc code=end
