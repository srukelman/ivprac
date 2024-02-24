'''
Runtime: beats 51.44%
Memory: beats 21.08%
'''

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = set()
        for i in nums:
            if i in l:
                l.remove(i)
            else:
                l.add(i)
        return list(l)[0]