# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return countNode(root)
def heightleft(node):
    height = 0
    while node:
        height += 1
        node = node.left
    return height
def heightright(node):
    height = 0
    while node:
        height += 1
        node = node.right
    return height
def countNode(root):
    if root == None:
        return 0
    lh = heightleft(root)
    rh = heightright(root)
    if lh == rh:
        return (1<<lh)-1
    else:
        return 1 + countNode(root.left) + countNode(root.right)