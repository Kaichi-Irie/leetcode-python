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
        self.preorder_root_index = 0
        inorder_val_to_index = {val:i for i, val in enumerate(inorder)}
        def array_to_tree(left, right) -> TreeNode|None:
            if left>right:
                return None
            root_val = preorder[self.preorder_root_index]
            self.preorder_root_index += 1
            root_index = inorder_val_to_index[root_val]
            root = TreeNode(val=root_val)
            root.left = array_to_tree(left,root_index-1)
            root.right = array_to_tree(root_index+1, right)
            return root
        return array_to_tree(0, len(inorder)-1)




# @lc code=end
