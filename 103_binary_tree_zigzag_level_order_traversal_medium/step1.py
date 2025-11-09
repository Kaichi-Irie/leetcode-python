#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root) -> list[list[int]]:
        if not root:
            return []
        LEFT_TO_RIGHT = 1
        RIGHT_TO_LEFT = -1
        direction = LEFT_TO_RIGHT
        nodes = [root]
        zigzag_level_nodes = []
        while nodes:
            node_vals = []
            next_level_nodes = []
            while nodes:
                node = nodes.pop()
                node_vals.append(node.val)
                if direction == LEFT_TO_RIGHT:
                    if node.left:
                        next_level_nodes.append(node.left)
                    if node.right:
                        next_level_nodes.append(node.right)
                else:
                    if node.right:
                        next_level_nodes.append(node.right)
                    if node.left:
                        next_level_nodes.append(node.left)

            zigzag_level_nodes.append(node_vals)
            nodes = next_level_nodes
            direction *= -1
        return zigzag_level_nodes


# @lc code=end
