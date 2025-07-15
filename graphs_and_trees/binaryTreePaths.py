# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        all_paths=[]
        if root is None:
            return []
        def dfs(node,curr_path):
            if node is None:
                return node
            if not curr_path:
                curr_path+=str(node.val)
            else:
                curr_path+="->"+str(node.val)
            if node.left is None and node.right is None:
                all_paths.append(curr_path)
                return
            dfs(node.left,curr_path)
            dfs(node.right,curr_path)
        dfs(root,"")
        return all_paths

            