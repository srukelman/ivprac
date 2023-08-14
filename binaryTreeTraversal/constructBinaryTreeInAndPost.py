# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {val:i for i, val in enumerate(inorder)}

        pos = len(postorder)-1
        def buildTree(lp, rp):
            nonlocal pos
            if pos < 0 or lp > rp:
                return None
            root = TreeNode(postorder[pos])
            pos -= 1
            i = d[root.val]
            root.right = buildTree(i+1, rp)                    
            root.left = buildTree(lp, i-1)
            return root

        return buildTree(0, pos)