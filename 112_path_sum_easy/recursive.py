#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def is_leaf(root) -> bool:
            return root.left is None and root.right is None

        def dfs(root, path_sum) -> bool:
            if is_leaf(root):
                path_sum += root.val
                if path_sum == targetSum:
                    return True
                else:
                    return False
            path_sum += root.val
            res_left = False
            if root.left is not None:
                res_left = dfs(root.left, path_sum)
            res_right = False
            if root.right is not None:
                res_right = dfs(root.right, path_sum)
            return res_left or res_right

        if root is None:
            return False
        return dfs(root, 0)


# @lc code=end
