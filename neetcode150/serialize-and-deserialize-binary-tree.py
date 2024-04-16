# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    i = 0
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.preOrderSerialize(root)
        
    def preOrderSerialize(self, node):
        if not node:
            return 'N'

        return ','.join([str(node.val), self.preOrderSerialize(node.left), self.preOrderSerialize(node.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.preOrderUnserialize(data.split(','))
    
    def preOrderUnserialize(self, elems):
        if elems[self.i] == 'N':
            self.i += 1
            return None
        
        node = TreeNode(elems[self.i])
        self.i += 1

        node.left = self.preOrderUnserialize(elems)
        node.right = self.preOrderUnserialize(elems)

        return node



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))