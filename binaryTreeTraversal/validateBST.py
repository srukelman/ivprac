# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return helper(root, -2e63, 2e63-1)
def helper(node, start, end) -> bool:
    if node == None:
        return True
    if node.val <= start or node.val >= end:
        return False
    return helper(node.left, start, node.val) and helper(node.right, node.val, end)