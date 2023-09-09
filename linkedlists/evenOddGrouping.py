'''
Runtime: beats 82.15%
Memory Usage: beats 51.74%
'''

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        currodd,curreven,heade = head, head.next,head.next        
    
        while curreven and curreven.next:
            currodd.next = currodd.next.next
            curreven.next = curreven.next.next
            currodd = currodd.next
            curreven = curreven.next  
        currodd.next = heade
        return head  
        

        