'''
Runtime: beats 81.52%
Memory Usage: beats 25.09%
'''
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []

        result = [-1] * len(nums)

        for _ in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    result[stack.pop()] = nums[i]
                stack.append(i)
        return result