#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ret = None
        self.k = k
        self.find_small(root)
        return self.ret
    
    def find_small(self, node):
        if not node: return 
        
        self.find_small(node.left)

        self.k -= 1
        if self.k == 0:
            self.ret = node.val
            return
        
        self.find_small(node.right)
        
# @lc code=end

