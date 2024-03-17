import unittest
class ListNode:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def getListfromHead(self, head):
        result = []
        while head:
            result.append(head.value)
            head = head.next
        return result

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        return prev
    
class TestReverseDoubleLinkedList(unittest.TestCase):
    def test_reverse_double_linked_list(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        solution = Solution()
        result = solution.reverseList(head)
        self.assertEqual(ListNode().getListfromHead(result), [4, 3, 2, 1])
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = solution.reverseList(head)
        self.assertEqual(ListNode().getListfromHead(result), [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()