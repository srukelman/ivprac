'''
Runtime: beats 99.18%
Memory Usage: beats 94.76%
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merge = ""
        while i < len(word1) or i < len(word2):
            if i >= len(word1):
                merge += word2[i:]
                break
            if i >= len(word2):
                merge += word1[i:]
                break
            merge += word1[i]
            merge += word2[i]
            i += 1
        return merge