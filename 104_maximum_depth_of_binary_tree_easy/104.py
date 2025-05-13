#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


# from math import inf
# from functools import cache
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0
            depth_left = dfs(node.left)
            depth_right = dfs(node.right)
            return max(depth_left, depth_right) + 1

        return dfs(root)


# @lc code=end
