#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def recoverTree(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     self.first = None
    #     self.second = None
    #     self.prev = None
    #     self.inorder(root)
    #     self.first.val, self.second.val = self.second.val, self.first.val

    # def inorder(self, root):
    #     if not root:
    #         return
    #     self.inorder(root.left)
    #     if self.prev and self.prev.val > root.val:
    #         if not self.first:
    #             self.first = self.prev
    #         self.second = root
    #     self.prev = root
    #     self.inorder(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:

        res = []

        self.inorder(root,res)
        first,second = None, None
        for i in range(len(res)-1):

            # find the first node which disobeys inorder rule
            if res[i].val > res[i+1].val and not first:
                first = res[i]
            
            # find the second node which disobeys inorder rule
            if res[i].val > res[i+1].val and first:
                second = res[i+1]

        first.val, second.val = second.val, first.val


    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root)
            self.inorder(root.right, res)


        

        
# @lc code=end

