'''
Runtime: beats 46.03%
Memory Usage: beats 7.25%
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        stack = []
        curr = head
        for i in range(n//2):
            stack.append(curr)
            curr = curr.next
        maxsum = -1
        while stack and curr:
            maxsum = max(stack.pop().val + curr.val, maxsum)
            curr = curr.next
        return maxsum
        