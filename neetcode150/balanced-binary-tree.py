# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isBalanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

    # Solution-1: O(n) solution
    #     self.getMaxHeight(root)

    #     return self.isBalanced

    # def getMaxHeight(self, node):
    #     if not node:
    #         return -1

    #     left = 1 + self.getMaxHeight(node.left)
    #     right = 1 + self.getMaxHeight(node.right)

    #     if abs(left - right) > 1:
    #         self.isBalanced = False

    #     return max(left, right)

    # Solution-2: Hacky Solution: use exception to break out of recursion just when the condition is true. Saves a lot of backtracking in best and average cases
        try:
            self.getMaxHeight(root)
            
            return True
        except:
            return False

    def getMaxHeight(self, node):
        if not node:
            return -1

        left = 1 + self.getMaxHeight(node.left)
        right = 1 + self.getMaxHeight(node.right)

        if abs(left - right) > 1:
            raise Exception(False)

        return max(left, right)

        
        