'''
Runtime: beats 98.31%
Memory Usage: beats 44.71%
'''
from typing import List
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter([tuple(row) for row in grid])
        return sum([rows[col] for col in zip(*grid)])