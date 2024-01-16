'''
Runtime: 648ms - beats 91.48%
Memory Usage: 18.98MB - beats 21.08%
'''

from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x = entrance[1]
        y = entrance[0]
        queue = deque()
        queue.appendleft((x, y, 0))
        visited = set()
        visited.add((x,y))
        while queue:
            x, y, step = queue.pop()
            if x == 0 or x == len(maze[0]) - 1 or y == 0 or y == len(maze) - 1:
                if step != 0:
                    return step
            if x > 0 and (x-1, y) not in visited and maze[y][x-1] == ".":
                queue.appendleft((x-1, y, step + 1))
                visited.add((x-1,y))
            if x < len(maze[0]) - 1 and (x+1, y) not in visited and maze[y][x+1] == ".":
                    queue.appendleft((x+1, y, step + 1))
                    visited.add((x+1,y))
            if y < len(maze) -1 and (x, y+1) not in visited and maze[y+1][x] == ".":
                queue.appendleft((x, y+1, step + 1))
                visited.add((x, y+1))
            if y > 0 and (x, y-1) not in visited and maze[y-1][x] == ".":
                queue.appendleft((x, y-1, step + 1))
                visited.add((x, y-1))
        return -1
            

        