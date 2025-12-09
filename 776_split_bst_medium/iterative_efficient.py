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
        small_dummy = TreeNode()
        large_dummy = TreeNode()

        node = root
        small_node = small_dummy
        large_node = large_dummy
        while node is not None:
            if node.val <= target:
                small_node.right = node
                small_node = node
                next_node = node.right
                node.right = None
                node = next_node
            else:
                large_node.left = node
                large_node = node
                next_node = node.left
                node.left = None
                node = next_node

        return [small_dummy.right, large_dummy.left]

# @lc code=end
