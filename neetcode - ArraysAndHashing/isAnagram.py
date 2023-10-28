'''
Runtime: beats 90.53%
Memory Usage: beats 18.16%%
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)