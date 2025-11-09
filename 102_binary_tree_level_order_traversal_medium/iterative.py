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


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        node_queue = deque([(root, 0)])  # (node,level)
        level_to_values: list[list[int]] = []
        while node_queue:
            node, level = node_queue.popleft()
            while len(level_to_values) <= level:
                level_to_values.append([])
            level_to_values[level].append(node.val)
            if node.left:
                node_queue.append((node.left, level + 1))
            if node.right:
                node_queue.append((node.right, level + 1))

        return level_to_values


# @lc code=end
