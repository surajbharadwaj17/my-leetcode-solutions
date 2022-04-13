"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):

        # find len of linked list
        n = 0
        temp = head
        while(temp):
            n += 1
            temp = temp.next

        if n == 1:
            return None

        # deleting the mid
        cnt, mid = 0, n//2
        prev, cur = None, head

        while(cur and cnt <= mid):
            if cnt == mid:
                # mid node case
                nxt = cur.next
                prev.next = nxt
            else:
                prev = cur
                cur = cur.next

            cnt += 1

        return head