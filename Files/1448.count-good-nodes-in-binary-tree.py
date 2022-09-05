#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, max_good=-10000) -> int:
        if not root: return 0
        res = 0
        if root.val >= max_good:
            res = 1
        else:
            res = 0

        max_good = max(max_good, root.val)

        res += self.goodNodes(root.left, max_good)
        res += self.goodNodes(root.right, max_good)

        return res

        
# @lc code=end

