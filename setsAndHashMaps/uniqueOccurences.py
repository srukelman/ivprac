from collections import defaultdict
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for i in arr:
            d[i] += 1
        s = set()
        for k in d.keys():
            x = len(s)
            s.add(d[k])
            if x == len(s):
                return False
        return True