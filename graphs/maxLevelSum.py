'''
Runtime: beats 65.63%
Memory Usage: beats 41.89%
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        lvl, min_level_so_far, max_sum_so_far = 0, 0, float('-inf')        
        q = [root]

        while(len(q) > 0):
            n = len(q)
            curr_sum = 0
            lvl += 1

            while n > 0:
                n -= 1
                node = q.pop(0)
                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum_so_far < curr_sum:
                min_level_so_far = lvl
                max_sum_so_far = curr_sum

        return min_level_so_far