from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        leftSum = 0
        rightSum = sum(nums[1:])
        while leftSum != rightSum:
            leftSum += nums[pivot]
            pivot+= 1
            rightSum -= nums[pivot]
            if(pivot == len(nums) - 1):
                if rightSum != leftSum:
                    return -1
        return pivot
        