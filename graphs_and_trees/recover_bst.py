# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first_swap=None
        self.second_swap=None
        self.prev_node=None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.prev_node is not None and self.prev_node.val>node.val:
                if self.first_swap is None:
                    self.first_swap=self.prev_node
                self.second_swap=node
            self.prev_node=node
            dfs(node.right)
        dfs(root)
        if self.first_swap and self.second_swap:
            self.first_swap.val,self.second_swap.val=self.second_swap.val,self.first_swap.val



'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.
 Recover the tree without changing its structure.
'''