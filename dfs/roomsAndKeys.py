'''
Runtime: beats 55.13%
Memory Usage: beats 84.98%
'''
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visitableRooms = set()
        while stack:
            curr = stack.pop()
            visitableRooms.add(curr)
            for key in rooms[curr]:
                if key not in visitableRooms:
                    stack.append(key)
        return visitableRooms == set(range(len(rooms)))
