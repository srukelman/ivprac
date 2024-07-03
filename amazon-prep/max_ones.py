from typing import List
class Solution: 
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        maxlen = 0
        for index, j in enumerate(nums):
            if j == 0:
                maxlen = max(maxlen, index - i)
                i = index + 1
        return max (maxlen, len(nums) - i)