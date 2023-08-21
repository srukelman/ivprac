'''
Runtime: 95.75%
Memory Usage: 56.91%
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        ans = ""
        for i in range(0, len(arr)):
            if len(arr[len(arr)-i - 1]) > 0:
                ans += arr[len(arr) - i -1] + " "
        return ans[:-1]