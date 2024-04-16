# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maximum = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.getMaxSum(root)
        return self.maximum

    def getMaxSum(self, node):
        if not node:
            return 0

        leftSum = self.getMaxSum(node.left)
        rightSum = self.getMaxSum(node.right)

        # return max left or right chain or a combination of current with left and/or right
        # self.maximum = max(self.maximum, node.val, node.val + leftSum, node.val + rightSum, node.val + leftSum + rightSum)
        self.maximum = max(self.maximum, node.val + leftSum + rightSum)

        # return longest chain: either left chain or right chain or node itself
        # return max(node.val, leftSum + node.val, rightSum + node.val)
        return max(node.val, leftSum + node.val, rightSum + node.val, 0)