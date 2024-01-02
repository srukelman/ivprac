'''
Runtime: beats 49.35%
Memory Usage: beats 92.49%
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        currRow = [root]
        nextRow = []
        maxes = []
        while currRow:
            currMax = currRow[0].val
            for node in currRow:
                if node.left:
                    nextRow.append(node.left)
                if node.right:
                    nextRow.append(node.right)
                currMax = max(currMax, node.val)
            maxes.append(currMax)
            currRow, nextRow = nextRow, []
        return maxes
        