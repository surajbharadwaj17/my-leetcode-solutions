"""
Given the head of a linked list, sort the list using insertion sort and 
return the head of the sorted linked list.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def insertionSortList(self, head):
        if not head:
            return

        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                prev = dummy
                while prev.next.val < cur.next.val:
                    prev = prev.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = prev.next
                prev.next = tmp
            else:
                cur = cur.next
        return dummy.next

