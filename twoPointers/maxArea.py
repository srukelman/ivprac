'''
Runtime: beats 57.90%
Memory Usage: beats 8.74%
'''
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        areaMax  = 0
        begin = 0
        end = len(height) - 1
        while end > begin:
            curr = (min(height[end], height[begin]) * (end - begin))
            areaMax = max(areaMax, curr)
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1
        return areaMax
            