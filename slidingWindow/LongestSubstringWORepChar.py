class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        begin = 0
        end = 0
        maxlen = 0
        prevend = -1
        while(end < len(s)):
            charb = s[begin]
            chare = s[end]
            try:
                if(prevend != end):
                    d[chare] += 1   
            except:
                d[chare] = 1
            prevend = end
            if(d[chare] > 1):
                begin += 1
                if(begin > end):
                    end = begin
                d[charb] -= 1
            else:
                end += 1
                if(maxlen < (end-begin)):
                    maxlen = end-begin
        if(maxlen < (end-begin)):
            maxlen = end-begin
        return maxlen