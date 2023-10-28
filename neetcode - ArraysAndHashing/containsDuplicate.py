'''
Runtime: beats 95.17%
Memory Usage: beats 86.15%
'''
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)