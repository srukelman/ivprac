'''
Runtime: beats 89.12% (43ms)
Memory Usage: beats 10.97% (17.92MB)
'''
from typing import List

class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        l = 0
        r = len(nums) * len(nums[0])
        while l < r:
            m = l + (r - l) // 2
            i = m // len(nums[0])
            j = m % len(nums[0])
            if nums[i][j] == target:
                return True
            if nums[i][j] < target:
                l = m + 1
            else:
                r = m
        return False