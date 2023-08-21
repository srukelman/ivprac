'''
Runtime: 88.37%
Memory Usage:  34.44%
'''
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCan = -1
        for i in candies:
            if i > maxCan:
                maxCan = i
        r = list()
        for i in candies:
            r.append(i + extraCandies >= maxCan)
        return r   