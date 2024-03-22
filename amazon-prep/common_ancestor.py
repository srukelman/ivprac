from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node: return None
            if node in [p, q]: return node
            l, r = get_lca(node.left), get_lca(node.right)
            if l and r: return node
            return l or r

        return get_lca(root)