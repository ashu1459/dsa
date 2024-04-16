# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTSubree(root, float("-infinity"), float("infinity"))
    
    def isValidBSTSubree(self, node, leftBoundary, rightBoundary):
        if not node:
            return True

        if not (leftBoundary < node.val < rightBoundary):
            return False
        
        return self.isValidBSTSubree(node.left, leftBoundary, node.val) and self.isValidBSTSubree(node.right, node.val, rightBoundary)