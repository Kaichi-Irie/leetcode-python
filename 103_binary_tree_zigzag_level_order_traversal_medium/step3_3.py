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
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        zigzag_level_order_vals: list[list[int]] = []  # deque
        nodes = [root]
        next_level_nodes = []
        level = 0

        while True:
            zigzag_vals = []
            for node in nodes:
                if node is None:
                    continue
                zigzag_vals.append(node.val)
                next_level_nodes.append(node.left)
                next_level_nodes.append(node.right)

            if not next_level_nodes:
                return zigzag_level_order_vals
            # align node vals from right to left
            if level % 2 == 1:
                zigzag_vals.reverse()
            zigzag_level_order_vals.append(zigzag_vals)
            nodes = next_level_nodes
            next_level_nodes = []
            level += 1


# @lc code=end
