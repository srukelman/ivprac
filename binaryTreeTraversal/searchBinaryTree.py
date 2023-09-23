'''
Runtime: beats 86.31%
Memory Usage: beats 64.98%
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while True:
            if root.val == val:
                return root
            if root.val > val:
                if not root.left:
                    return None
                else:
                    root = root.left
            else:
                if not root.right:
                    return None
                else:
                    root = root.right

        