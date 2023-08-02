#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ret = [0]
        self.dfs(root, root.val, root.val, ret)
        return ret[0]

    def dfs(self, root, low, high, ret):
        if not root: return 

        ret[0] = max(ret[0], abs(root.val - low), abs(root.val - high))

        if root.val < low:
            low = root.val

        if root.val > high:
            high = root.val

        self.dfs(root.left, low, high, ret)
        self.dfs(root.right, low, high, ret)
        
# @lc code=end

