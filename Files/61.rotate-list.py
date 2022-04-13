#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (33.72%)
# Likes:    4200
# Dislikes: 1242
# Total Accepted:    492.4K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Approach 1: Link the last element to the first and move the head ahead k places
        # cur = head
        # n = 0
        # while(cur.next):
        #     cur = cur.next
        #     n += 1

        # cur.next = head

        # for _ in range(n-k):
        #     head = head.next

        # return head

        if not head: return
        cur = head
        n = 1
        
        while(cur.next):
            cur = cur.next
            n+= 1

        
        if n==1 or k==0:
            return head

        

        k = k%n
        cur.next = head
        temp = head

        for _ in range(n-k-1):
            temp = temp.next

        ret = temp.next
        temp.next = None

        return ret


# @lc code=end

