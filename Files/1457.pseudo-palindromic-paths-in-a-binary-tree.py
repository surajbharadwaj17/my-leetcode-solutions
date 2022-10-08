#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from logging import RootLogger


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        """
        Traverse a tree and maintain a set if there is even count or odd count

        * Remove from the set if there is a same element in the set because they are a pair match
        * In the leaf, if set is empty then even palindromic
        * If set has 1 element then odd palindromic
        * If the set has more than one elements, then it is not a palindrome
        """
        def dfs(node, visited):
            if not node:
                return 0
            
            visited.remove(node.val) if node.val in visited else visited.add(node.val)
            count = 0
            if not node.left and not node.right:
                if len(visited) <= 1:
                    count = 1
            else:
                count = count + dfs(node.left, visited) + dfs(node.right, visited)
            
            visited.remove(node.val) if node.val in visited else visited.add(node.val)
            return count

        return dfs(root, set())
                    






# @lc code=end

