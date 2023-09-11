'''
Runtime: Beats 82.24%
Memory Usage: beats 74.10%
'''
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # edge case - only 2 nodes
        if not head.next.next:
            return head.val + head.next.val 

        # find midpoint of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # compute sum of nodes
        maxSum = 0
        left, right = head, prev
        while left and right:
            tmpSum = left.val + right.val
            if tmpSum > maxSum:
                maxSum = tmpSum
            else:
                left = left.next
                right = right.next
        
        return maxSum