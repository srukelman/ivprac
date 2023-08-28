'''
Runtime: beats 71.98%
Memory Usage: beats 56.14%
'''
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_count=0
        cur_count=0
        max_count=0
        if 0 not in nums:
            return len(nums)-1
        if 1 not in nums:
            return 0
        for j in nums:
            if j==1:
                cur_count+=1
            else:
                max_count=max(max_count,prev_count+cur_count)
                prev_count=cur_count
                cur_count=0
        return max(max_count,prev_count+cur_count)