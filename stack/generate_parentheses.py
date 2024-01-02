'''
Runtime: beats 10.58% (56 ms)
Memory Usage: beats 19.70% (17.5 MB)
'''
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 
            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')
        res = []
        dfs(0, 0, '')
        pass
        return res
