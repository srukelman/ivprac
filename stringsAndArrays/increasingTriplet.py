'''
Runtime: 95.13%
Memory Usage: 25.52%
'''
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f= float('inf')
        s = float('inf')
        for n in nums:
            if n <= f:
                f = n
            elif n <= s:
                s = n
            elif n > s:
                return True
        return False