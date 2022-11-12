#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0

        # Collecting first number
        while(l1):
            num1 *= 10
            num1 += l1.val
            l1 = l1.next

        # Collecting second number
        while(l2):
            num2 *= 10
            num2 += l2.val
            l2 = l2.next

        # Add
        total = num1+num2

        # Rebuild
        head = None
        prev = None

        while total > 0:
            head = ListNode(val=total%10)
            head.next = prev
            prev = head
            total = total//10

        ## Head and prev pointers movements
        """
            7243 
             564
            
            7       0                0                  8               8           7
            prev  <--  head    =>    prev      <--     head     =>      prev  <-- head
        """

        if head:
            return head
        else:
            return ListNode(0)

        
# @lc code=end

