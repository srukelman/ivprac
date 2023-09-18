'''
Runtime: beats 78.65%
Memory Usage: beats 59.19%
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root: Optional[TreeNode]) ->List[int]:
            queue = [root]
            leaves = []
            while queue:
                curr = queue.pop()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if not (curr.left or curr.right):
                    leaves.append(curr.val)
            return leaves
        return (getLeaves(root1)==getLeaves(root2))