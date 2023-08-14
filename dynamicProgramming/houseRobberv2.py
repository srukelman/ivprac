from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev1 = 0
        prev2 = 0
        for i in nums:
            temp = prev1
            prev1 = max(prev2 + i, prev1)
            prev2 = temp
        return prev1