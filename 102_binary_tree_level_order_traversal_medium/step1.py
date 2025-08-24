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


from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        level_to_values: dict[int, list[int]] = defaultdict(list)

        def search(node: TreeNode | None, level: int) -> None:
            if not node:
                return
            level_to_values[level].append(node.val)
            if node.left:
                search(node.left, level + 1)
            if node.right:
                search(node.right, level + 1)

        search(root, 0)
        num_levels = len(level_to_values)
        level_to_values_list = [[] for _ in range(num_levels)]
        for level, values in level_to_values.items():
            level_to_values_list[level] = values
        return level_to_values_list


# @lc code=end
