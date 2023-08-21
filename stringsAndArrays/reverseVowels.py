'''
Runtime: 86.36%
Memory Usage: 85.21%
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = ('a', 'e', 'i', 'o', 'u')
        s = list(s)
        while (l < r):
            if s[l].lower() not in vowels:
                l += 1
            elif s[r].lower() not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)