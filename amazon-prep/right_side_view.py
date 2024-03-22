from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.val]
        curr_row = deque()
        result = []
        curr_row.append(root)
        while curr_row:
            next_row = deque()
            prev = -1
            for curr in curr_row:
                if curr.left:
                    next_row.append(curr.left)
                if curr.right:
                    next_row.append(curr.right)
                prev = curr
            result.append(prev.val)
            
            curr_row = next_row
        
        return result