#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math

class Solution:
    def isValidBST(self, root: TreeNode|None) -> bool:
        def is_valid(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return is_valid(root.left, lower, root.val) and is_valid(root.right, root.val, upper)

        return is_valid(root, -math.inf, math.inf)

# @lc code=end
