#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode|None) -> bool:
        if root is None:
            return True
        def find_validity_and_minmax(root: TreeNode) -> tuple[bool, int, int]:
            min_val = max_val = root.val
            if root.left is not None:
                is_left_valid, min_val, left_max = find_validity_and_minmax(root.left)
                if not is_left_valid or left_max >= root.val:
                    return False, 0, 0
            if root.right is not None:
                is_right_valid, right_min, max_val = find_validity_and_minmax(root.right)
                if not is_right_valid or root.val >= right_min:
                    return False, 0, 0
            return True, min_val, max_val
        is_valid, _, _ = find_validity_and_minmax(root)
        return is_valid

# @lc code=end
