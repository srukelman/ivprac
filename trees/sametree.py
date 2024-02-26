from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return not p and not q
        p_stack = [p]
        q_stack = [q]
        while p_stack and q_stack:
            p_curr = p_stack.pop(0)
            q_curr = q_stack.pop(0)
            if p_curr.val != q_curr.val:
                return False
            if p_curr.left and not q_curr.left:
                return False
            if not p_curr.left and q_curr.left:
                return False
            if p_curr.right and not q_curr.right:
                return False
            if not p_curr.right and q_curr.right:
                return False
            if p_curr.left:
                p_stack.append(p_curr.left)
            if p_curr.right:
                p_stack.append(p_curr.right)
            if q_curr.left:
                q_stack.append(q_curr.left)
            if q_curr.right:
                q_stack.append(q_curr.right)
            if len(p_stack) != len(q_stack):
                return False
        return not p_stack and not q_stack