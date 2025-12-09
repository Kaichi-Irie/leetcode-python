#
# @lc app=leetcode id=776 lang=python3
#
# [776] Split BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def splitBST(self, root: TreeNode|None, target: int) -> list[TreeNode|None]:
        if root is None:
            return [None, None]
        if root.val <= target:
            small, large = self.splitBST(root.right, target)
            root.right = small
            return [root, large]
        small, large = self.splitBST(root.left, target)
        root.left = large
        return [small, root]


# @lc code=end
