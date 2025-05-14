#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#


from typing import List, Optional
from math import inf
from functools import cache


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def merge(root1, root2):
            if root1 is None and root2 is None:
                return None
            new_node = TreeNode(left=None, right=None)
            if root1 is None:
                val1 = 0
                left1 = right1 = None
            else:
                val1 = root1.val
                left1 = root1.left
                right1 = root1.right

            if root2 is None:
                val2 = 0
                left2 = right2 = None
            else:
                val2 = root2.val
                left2 = root2.left
                right2 = root2.right

            new_node.val = val1 + val2
            new_node.left = merge(left1, left2)
            new_node.right = merge(right1, right2)
            return new_node

        return merge(root1, root2)


# @lc code=end
