from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return maxsize
            if i == j == 0:
                return grid[0][0]
            return grid[i][j] + min(dp(i - 1,j), dp(i, j - 1))
        return dp(len(grid) - 1, len(grid[0]) - 1)