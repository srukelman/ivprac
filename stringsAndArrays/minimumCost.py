'''
IBM Interview Question
Given an array of integers, the cost is the sum of the square of the differences between adjacent elements.
Insert a new integer into the array at any position, and return the minimum cost of doing so.
'''
import math
from typing import List
def minimumCost(arr: List[int]) -> int:
    maxdiff = 0
    index = -1
    left = -1
    right = -1
    insertval = -1
    for i in range (1, len(arr)):
        if maxdiff < abs(arr[i] - arr[i-1]):
            maxdiff = abs(arr[i] - arr[i-1])
            index = i
            left = arr[i-1]
            right = arr[i]
    cost = math.pow(right-insertval, 2)
    cost += math.pow(insertval-left, 2)
    for i in range(1, len(arr)):
        if i == index:
            continue
        cost += math.pow(arr[i] - arr[i-1], 2)
    return int(cost)