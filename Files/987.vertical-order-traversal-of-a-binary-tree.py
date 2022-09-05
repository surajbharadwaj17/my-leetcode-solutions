#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        import collections
        if not root: return []
        hmap = collections.defaultdict(list)
        level = [(root,0,0)]
        while level:
            for _ in range(len(level)):
                node, hd, vd = level.pop(0)
                hmap[hd].append((vd, node.val))
                if node.left:
                    level.append((node.left, hd-1, vd-1))
                if node.right:
                    level.append((node.right, hd+1, vd-1))
        ret = []
        for key in sorted(hmap.keys()):
            print(hmap[key])
            level = [x[1] for x in sorted(hmap[key], key=lambda x: (-x[0], x[1]))]
            ret.append(level)
        return ret

        
# @lc code=end

