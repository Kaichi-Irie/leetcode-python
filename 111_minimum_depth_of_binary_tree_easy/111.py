#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


from math import inf


# from functools import cache
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def is_leaf(root):
            return (root is not None) and (root.left is None) and (root.right is None)

        def dfs(root):
            if root is None:
                return inf
            elif is_leaf(root):
                return 1
            left_min_depth = dfs(root.left)
            right_min_depth = dfs(root.right)
            return min(left_min_depth, right_min_depth) + 1

        return dfs(root)


# @lc code=end
