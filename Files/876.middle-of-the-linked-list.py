#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1

        i = 0 
        cur = head
        while i < n//2:
            cur = cur.next
            i += 1

        return cur
        
# @lc code=end

