#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaf(root):
            if root.left or root.right:
                if root.left:
                    for key in get_leaf(root.left):
                        yield key
                if root.right:
                    for key in get_leaf(root.right):
                        yield key
            else:
                yield root.val

        return list(get_leaf(root1)) == list(get_leaf(root2))


# @lc code=end

