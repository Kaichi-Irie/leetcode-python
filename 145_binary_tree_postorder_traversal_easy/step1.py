#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode|None) -> list[int]:
        postorder_values = []
        def traverse(root: TreeNode|None):
            if root is None:
                return
            traverse(root.left)
            traverse(root.right)
            postorder_values.append(root.val)
        traverse(root)
        return postorder_values

# @lc code=end
