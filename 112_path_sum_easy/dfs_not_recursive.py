#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def is_leaf(root) -> bool:
            return (root.left is None) and (root.right is None)

        if root is None:
            return False

        stack = deque()
        stack.append((root, root.val))
        while len(stack) > 0:
            node, path_sum = stack.pop()
            print(f"{node=}, {path_sum=}")
            if is_leaf(node) and path_sum == targetSum:
                return True
            if node.left is not None:
                stack.append((node.left, node.left.val + path_sum))
            if node.right is not None:
                stack.append((node.right, node.right.val + path_sum))
        return False


# @lc code=end
