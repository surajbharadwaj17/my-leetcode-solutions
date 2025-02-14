#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return 'x'

        # Pre order and join to form a string

        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data
        if self.data[0] == 'x':
            return None

        node = TreeNode((self.data[:self.data.find(",")]))
        node.left = self.deserialize(self.data[self.data.find(",")+1:])
        node.right = self.deserialize(self.data[self.data.find(",")+1:])

        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

