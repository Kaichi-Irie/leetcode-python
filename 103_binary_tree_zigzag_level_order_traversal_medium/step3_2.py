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


from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        zigzag_node_vals: list[deque[int]] = []  # deque
        nodes_queue = deque([(root, 0)])
        while nodes_queue:
            node, level = nodes_queue.popleft()
            if node is None:
                continue
            while len(zigzag_node_vals) <= level:
                zigzag_node_vals.append(deque([]))
            if level % 2 == 0:  # from left to right; FIFO
                zigzag_node_vals[level].append(node.val)
            else:  # from right to left; LIFO
                zigzag_node_vals[level].appendleft(node.val)

            nodes_queue.append((node.left, level + 1))
            nodes_queue.append((node.right, level + 1))
        return [list(deq) for deq in zigzag_node_vals]


# @lc code=end
