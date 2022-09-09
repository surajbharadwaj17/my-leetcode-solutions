#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = []

        if root:
            ret += self.inorderTraversal(root.left)
            ret.append(root.val)
            ret += self.inorderTraversal(root.right)
        
        return ret
        
# @lc code=end

