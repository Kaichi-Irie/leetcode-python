#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        zigzag_node_vals: list[deque[int]] = [deque([])]  # deque
        nodes = [root]
        next_level_nodes = []
        level = 0

        while nodes:
            for node in nodes:
                if node is None:
                    continue
                next_level_nodes.append(node.left)
                next_level_nodes.append(node.right)
                # left to right; FIFO
                if level % 2 == 0:
                    zigzag_node_vals[level].append(node.val)
                else:  # right to left; LIFO
                    zigzag_node_vals[level].appendleft(node.val)
            nodes = next_level_nodes
            next_level_nodes = []
            level += 1
            zigzag_node_vals.append(deque([]))
        return [list(deq) for deq in zigzag_node_vals]


# @lc code=end
