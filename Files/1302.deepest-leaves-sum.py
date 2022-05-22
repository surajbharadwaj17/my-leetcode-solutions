#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            return max(dfs(node.left), dfs(node.right))+1

        self.ret = 0
        depth = dfs(root)
        

        def dfs2(node, dep):
            if not node:
                return
            if dep == depth:
                self.ret += node.val

            dfs2(node.left, dep+1)
            dfs2(node.right, dep+1)

        dfs2(root, 1)

        return self.ret
            

        
# @lc code=end

