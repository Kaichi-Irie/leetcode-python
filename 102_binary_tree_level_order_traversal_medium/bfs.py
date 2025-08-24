#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        level_to_values = []
        nodes = [root]
        while nodes:
            this_level_values = []
            child_nodes = []
            for node in nodes:
                if not node:
                    continue
                this_level_values.append(node.val)
                if node.left:
                    child_nodes.append(node.left)
                if node.right:
                    child_nodes.append(node.right)
            level_to_values.append(this_level_values)
            nodes = child_nodes
        return level_to_values


# @lc code=end
