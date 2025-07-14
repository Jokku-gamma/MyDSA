from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_bound=-float('inf')
        max_bound=float('inf')
        def dfs(min_bound,node,max_bound):
            if not node:
                return True
            if not min_bound<node.val<max_bound:
                return False
            lnodes=dfs(min_bound,node.left,node.val)
            rnodes=dfs(node.val,node.right,max_bound)
            return lnodes and rnodes
        return dfs(min_bound,root,max_bound)
    

'''Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.'''