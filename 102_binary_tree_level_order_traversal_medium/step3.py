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
        
        nodes = [root]
        level_order_node_vals = []
        while nodes:
            node_vals = []
            next_level_nodes = []
            for node in nodes:
                node_vals.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            level_order_node_vals.append(node_vals)
            nodes = next_level_nodes
        return level_order_node_vals


# @lc code=end
