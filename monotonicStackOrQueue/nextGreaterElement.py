'''
Runtime: beats 88.24%
Memory Usage: beats 6.49%
'''
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}

        for num in nums2:
            while stack and num > stack[-1]:
                popnum = stack.pop()
                d[popnum] = num
            stack.append(num)
        
        arr = []
        for x in nums1:
            if x in d:
                arr.append(d[x])
            else:
                arr.append(-1)
        return arr