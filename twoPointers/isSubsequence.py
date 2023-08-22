'''
Runtime: beats 72.36%
Memory Usage: beats 24.29%
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subLen = len(s)
        mainLen = len(t)
        i = 0
        j = 0
        while i < subLen and j < mainLen:
            if(s[i] == t[j]):
                i += 1
            j += 1
        return subLen == i