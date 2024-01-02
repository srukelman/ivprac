'''
Runtime: beats 93.54%  (195ms)
Memory Usage: beats 5.94% (19.04MB)
'''
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target == nums[mid]:
                return mid
            else:
                high = mid - 1
        return -1