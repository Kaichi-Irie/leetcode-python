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
        def is_valid(root, lower_bound, upper_bound) -> bool:
            if root is None:
                return True
            if not (lower_bound < root.val < upper_bound):
                return False
            left_validity = is_valid(root.left, lower_bound, root.val)
            right_validity = is_valid(root.right, root.val, upper_bound)
            return left_validity and right_validity

        return is_valid(root, -math.inf, math.inf)

# @lc code=end
