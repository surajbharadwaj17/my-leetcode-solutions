#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return
        
        # If you switch the head, the possible difference in the lengths of 2 lists is encountered.
        head1, head2 = headA, headB
        while head1 != head2:
            # if either pointer meets the end, switch the head and continue second traversal
            if not head1:
                head1 = headB
            else:
                head1 = head1.next
            
            if not head2:
                head2 = headA
            else:
                head2 = head2.next

        return head1 

        
# @lc code=end

