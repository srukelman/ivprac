'''
Runtime: beats 9.41% (493 ms)
Memory Usage: beats 6.66% (18.94 MB)
'''
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        if len(piles) == 1:
            return -(piles[0] // -h)
        def hours_to_eat(piles: List[int], eating_speed: int) -> int:
            return sum([-(pile // -eating_speed) for pile in piles])
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            time = hours_to_eat(piles, mid)
            if time == h:
                if mid > 1 and hours_to_eat(piles, mid - 1) == h:
                    high = mid - 1
                    continue
                return mid
            elif time > h:
                low = mid + 1
            else:
                if mid > 1 and hours_to_eat(piles, mid - 1) > h:
                    return mid
                high = mid - 1
        return low
        
