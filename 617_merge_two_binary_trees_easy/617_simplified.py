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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def merge(root1, root2):
            if root1 is None:
                return root2
            elif root2 is None:
                return root1

            new_node = TreeNode(left=None, right=None)
            new_node.val = root1.val + root2.val
            new_node.left = merge(root1.left, root2.left)
            new_node.right = merge(root1.right, root2.right)
            return new_node

        return merge(root1, root2)


# @lc code=end
