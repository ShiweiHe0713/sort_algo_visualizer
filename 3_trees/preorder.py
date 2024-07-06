from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:        
        """144. Binary Tree Preorder Traversal"""
        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                return 
            preorder.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        preorder = []
        dfs(root)
        return preorder

def cmp(a: int, b: int) -> int:
    return (a > b) - (a < b)

