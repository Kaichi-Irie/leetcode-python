#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        level_to_values: list[list[int]] = []

        def traverse_tree(node: TreeNode | None, level: int) -> None:
            if not node:
                return
            while len(level_to_values) <= level:
                level_to_values.append([])
            level_to_values[level].append(node.val)
            if node.left:
                traverse_tree(node.left, level + 1)
            if node.right:
                traverse_tree(node.right, level + 1)

        traverse_tree(root, 0)
        return level_to_values


# @lc code=end
