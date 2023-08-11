import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = collections.defaultdict(int)
        for i in t:
            dt[i] += 1
        m,n = len(s), len(t)
        need = len(dt)
        have = 0
        l,r = 0,0
        ms=""
        ma=float('inf')
        ds=collections.defaultdict(int)
        for r in range(m):
            ds[s[r]] += 1
            if dt.get(s[r],-1) == ds[s[r]]:
                have+=1
            while have == need and l<=r:
                if r-l+1 < ma:
                    ma=r-l+1
                    ms=s[l:r+1]
                if ds[s[l]] == dt.get(s[l], -1):
                    have -=1
                ds[s[l]] -= 1
                l+=1
        return ms