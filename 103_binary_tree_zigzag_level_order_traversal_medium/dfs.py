#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        nodes_by_level = []

        def traverse(node: TreeNode, level: int):
            while len(nodes_by_level) <= level:
                nodes_by_level.append(deque([]))
            if level % 2 == 0:
                nodes_by_level[level].append(node.val)
            else:
                nodes_by_level[level].appendleft(node.val)

            if node.left:
                traverse(node.left, level + 1)
            if node.right:
                traverse(node.right, level + 1)

        traverse(root, 0)

        return [list(d) for d in nodes_by_level]


# @lc code=end
