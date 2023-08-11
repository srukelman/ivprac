from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        mid = 0
        high = len(nums) -1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] < target:
                if mid == len(nums)-1 or nums[mid + 1] > target:
                    return mid + 1
                low = mid + 1
            elif nums[mid] > target:
                if(mid == 0):
                    return 0
                high = mid -1
            else:
                return mid
        return -1