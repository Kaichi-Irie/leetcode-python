#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode|None:
        def constract_tree(preorder, inorder) -> TreeNode|None:
            if not preorder:
                return None
            root_val = preorder[0]
            for root_index in range(len(inorder)):
                if inorder[root_index] == root_val:
                    break

            left_inorder = inorder[:root_index]
            right_inorder = inorder[root_index+1:]
            left_vals = set(left_inorder)
            right_vals = set(right_inorder)
            left_preorder = [val for val in preorder if val in left_vals]
            right_preorder = [val for val in preorder if val in right_vals]

            root = TreeNode(val = root_val)
            root.left = constract_tree(left_preorder, left_inorder)
            root.right = constract_tree(right_preorder, right_inorder)
            return root
        return constract_tree(preorder, inorder)

# @lc code=end
