# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maximum = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.getMax(root)

        return self.maximum

    def getMax(self, node):
        if not node:
            return -1

        left = self.getMax(node.left) + 1
        right = self.getMax(node.right) + 1

        self.maximum = max(self.maximum, left + right)
        
        return max(left, right)
        
        