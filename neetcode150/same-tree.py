# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    identical = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Solution-0: O(p+q)
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

    #     # Solution-1: hacky approach. break out of recursion when False condition met
    #     try:
    #         self.isIdentical(p, q)
    #         return True
    #     except:
    #         return False
        
    #     # solution-2: O(n)
    #     # self.isIdentical(p, q)
    #     # return self.identical
    
    # def isIdentical(self, node1, node2):        
    #     if node1 and node2 and node1.val == node2.val:
    #         self.isIdentical(node1.left, node2.left)
    #         self.isIdentical(node1.right, node2.right)                
    #     else:
    #         if not node1 and not node2:
    #             return
    #         else:
    #             # solution-1: un-comment
    #             raise Exception(False)
    #             # solution-2: un-comment
    #             # self.identical = False
            

        