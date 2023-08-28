'''
Runtime: beats 96.61%
Memory Usage: beats 21.29%
'''
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        min_heap = [(0, k)]
        visited = set()
        distance = {i: float('inf') for i in range(1, n+1)}
        distance[k] = 0

        while min_heap:
            cur_total_time, cur_node = heapq.heappop(min_heap)
            if cur_node not in visited:
                visited.add(cur_node)

                for adj_node, adj_time in graph[cur_node]:
                    if cur_total_time + adj_time < distance[adj_node]:
                        distance[adj_node] = cur_total_time + adj_time
                        heapq.heappush(min_heap, (cur_total_time + adj_time, adj_node))
        return max(distance.values()) if len(visited) == n else -1

        