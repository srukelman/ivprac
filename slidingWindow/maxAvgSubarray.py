'''
Runtime: beats 97.58%
Memory Usage: beats 10.58%
'''
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = curr = sum(nums[:k])
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            if curr > best:
                best = curr
            
        return best / k