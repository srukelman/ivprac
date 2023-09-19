'''
Runtime: beats 84.61%
Memory Usage: beats 65.60%
'''
# Definition for a binary tree node.
from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float('-inf'), 0, 0
        q = deque()
        q.append(root)

        while q:
            level += 1
            tmp_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                tmp_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum < tmp_sum:
                max_sum, ans = tmp_sum, level
        
        return ans