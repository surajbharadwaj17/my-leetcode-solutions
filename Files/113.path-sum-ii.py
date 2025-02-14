#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        ret = []
        stack = [(root, targetSum-root.val, [root.val])]

        while stack:
            node, val, path = stack.pop()
            if not node.left and not node.right and val == 0:
                ret.append(path)
            if node.left:
                stack.append((node.left, val-node.left.val, path+[node.left.val]))
            if node.right:
                stack.append([node.right, val-node.right.val, path+[node.right.val]])

        return ret
# @lc code=end

