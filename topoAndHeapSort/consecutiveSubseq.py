'''
Runtime: beats 91.17%
Memory Usage: beats 74.64%
'''
from collections import deque
from typing import List
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        lower = min(nums)
        upper = max(nums)
        count = [0] * (upper - lower + 2)
        for x in nums:
            count[x - lower] += 1
        active = deque()
        for i in range(upper - lower + 2):
            while len(active) > count[i]:
                if i - active.popleft() < 3:
                    return False
            while len(active) < count[i]:
                active.append(i)
        return True