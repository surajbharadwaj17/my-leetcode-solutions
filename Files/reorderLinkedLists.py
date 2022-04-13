"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

"""

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head) -> None: 
        # Modify head in-place. No return required
        
        if not head:
            return
        
        temp, heap, n = head, [], 0
        while(temp):
            heap.append(temp.val)
            temp = temp.next
            n += 1

        left,right,cnt = 1,n-1,0
        dummy = ListNode(val = None)
        dummy.next = head
        temp = head
        while(left <= right):
            if cnt%2 != 0:
                new = ListNode(val = heap[left])
                left += 1
            else:
                new = ListNode(val = heap[right])
                right -= 1

            cnt += 1
            temp.next = new
            temp = temp.next

        return dummy.next

    
    def reorderList_v2(self, head) -> None:

        if not head: 
            return

        # find mid
        slow, fast = head, head
        while( fast.next and fast.next.next ):
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev, cur = None, slow.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # merge lists
        head1, head2 = head, prev
        while head2:
            nxt1 = head1.next
            head1.next = head2
            head1 = head2 
            head2 = nxt1
            

        