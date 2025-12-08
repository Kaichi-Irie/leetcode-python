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
        inorder_val_to_index = {val:i for i, val in enumerate(inorder)}
        def construct_tree(preorder_left, preorder_right,inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            if inorder_left > inorder_right:
                return None
            root_val = preorder[preorder_left]
            root = TreeNode(val=root_val)
            root_index = inorder_val_to_index[root_val]
            left_subtree_size = root_index - inorder_left
            root.left = construct_tree(preorder_left+1, preorder_left+left_subtree_size,inorder_left, root_index-1)
            root.right = construct_tree(preorder_left+left_subtree_size+1, preorder_right, root_index+1,inorder_right)
            return root
        return construct_tree(0, len(preorder)-1, 0, len(inorder)-1)

# @lc code=end
