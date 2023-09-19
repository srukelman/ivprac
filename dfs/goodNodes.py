'''
Runtime: beats 62.09%
Memory Usage: beats 90.46%
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            if not node:
                return 0
            
            output = 0
            if node.val>=maxval:
                output = 1 
            maxval=max(maxval,node.val)
            output+=dfs(node.left,maxval)
            output+=dfs(node.right,maxval)
            return output
        return dfs(root,root.val)
        
         