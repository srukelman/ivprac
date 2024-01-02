'''
Runtime: beats 73.03%
Memory Usage: beats 98.18%
'''
from typing import List
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = [], []
        for flower in flowers:
            starts.append(flower[0])
            ends.append(flower[1])
        starts.sort()
        ends.sort()
        blooming_flowers = {}
        people_copy = list(set(people))
        people_copy.sort()
        start_index = 0
        end_index = 0
        for person in people_copy:
            while start_index < len(starts) and starts[start_index] <= person:
                start_index += 1
            while end_index < len(ends) and ends[end_index] < person:
                end_index += 1
            blooming_flowers[person] = start_index - end_index
        for index, person in enumerate(people):
            people[index] = blooming_flowers[person]
        return people