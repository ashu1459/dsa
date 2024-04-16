# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    goodNodesCount = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.checkMax(root, root.val)

        return self.goodNodesCount

    def checkMax(self, node, maximum):
        if node.val >= maximum:
            self.goodNodesCount += 1
            maximum = node.val

        if node.left:
            self.checkMax(node.left, maximum)
        if node.right:
            self.checkMax(node.right, maximum)