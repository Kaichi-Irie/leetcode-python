#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        zigzag_level_nodes = []
        nodes = deque([(root, 0)])
        while nodes:
            next_nodes = deque([])
            while nodes:
                node, level = nodes.popleft()
                while len(zigzag_level_nodes) <= level:
                    zigzag_level_nodes.append(deque([]))

                # left to right
                if level % 2 == 0:
                    zigzag_level_nodes[level].append(node.val)
                # right to left
                else:
                    zigzag_level_nodes[level].appendleft(node.val)

                if node.left:
                    next_nodes.append((node.left, level + 1))
                if node.right:
                    next_nodes.append((node.right, level + 1))

            nodes = next_nodes

        return [list(deq) for deq in zigzag_level_nodes]


# @lc code=end
