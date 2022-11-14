#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            # Base case. If node is either p or q, return node
            if node == p or node == q:
                return node

            left, right = None, None
            if node.left: 
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)

            # If p and q are on either side 
            if left and right:
                return node
            else:
                # Either found will be the lowest descendant
                return left or right
        
        return dfs(root)
        
# @lc code=end

