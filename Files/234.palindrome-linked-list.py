#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (46.06%)
# Likes:    8256
# Dislikes: 508
# Total Accepted:    904.7K
# Total Submissions: 2M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        fast,slow = head, head

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        # slow is at mid node

        # Reverse the second half
        prev = None
        while(slow):
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:

            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next

        return True
        
# @lc code=end

