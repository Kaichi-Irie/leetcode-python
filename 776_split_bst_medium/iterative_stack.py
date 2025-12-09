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
        stack = [] # (node, is_greater)

        # append nodes to stack
        node = root
        while node is not None:
            if node.val <= target:
                stack.append((node, False))
                node = node.right
            else:
                stack.append((node, True))
                node = node.left

        small_node = None
        large_node = None

        while stack:
            node, is_large = stack.pop()
            if is_large:
                node.left = large_node
                large_node = node
            else:
                node.right = small_node
                small_node = node

        return [small_node, large_node]

# @lc code=end
