#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = root.val
        self.maxSum(root)
        return self.ret


    def maxSum(self, node):
        if not node: return 0

        left = max(0, self.maxSum(node.left))
        right = max(0, self.maxSum(node.right))

        self.ret = max(self.ret, left+node.val+right)
        return max(left, right) + node.val

        
# @lc code=end

