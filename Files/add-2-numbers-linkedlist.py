# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1,l2
        n1,n2, cnt = 0,0,0
        
        # Calculating the sum of 2 numbers
        while(head1):
            n1 += (10**cnt) * head1.val
            cnt +=1
            head1 = head1.next
            
        cnt = 0
        
        while(head2):
            n2 += (10**cnt) * head2.val
            cnt +=1
            head2 = head2.next
            
        ret = n1+n2

        # Creating the LL of ret
        ret_head = ListNode(ret%10)
        ret = ret//10
        
        temp = ret_head
        
        while(ret > 1):
            rem = ret % 10
            ret = ret//10
            new = ListNode(val=rem)
            temp.next = new
            temp = temp.next
            
        return ret_head
            

#s = Solution()


