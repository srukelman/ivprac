from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxSum = prefixSum = 0
        for i in gain:
            prefixSum += i
            maxSum = max(prefixSum, maxSum)
        return maxSum