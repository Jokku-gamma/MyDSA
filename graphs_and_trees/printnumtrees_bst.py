'''Given an integer n, return all the structurally 
unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
'''
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(left,right):
            if left>right:
                return [None]
            if left==right:
                return [TreeNode(left)]
            ans=[]
            for root in range(left,right+1):
                leftNodes=dfs(left,root-1)
                rightNodes=dfs(root+1,right)
                for lnode in leftNodes:
                    for rnode in rightNodes:
                        rootn=TreeNode(root,lnode,rnode)
                        ans.append(rootn)
            return ans
        return dfs(1,n)
