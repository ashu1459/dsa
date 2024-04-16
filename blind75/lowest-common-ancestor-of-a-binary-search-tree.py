# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # SOlution-1: using recursion. O(logn)
        # if p.val > q.val:
        #     return self.lowestCommonAncestor(root, q, p)

        # if p.val <= root.val <= q.val:
        #     return root

        # # both numbers are less than current node val
        # if q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return self.lowestCommonAncestor(root.right, p, q)

        # Solution-2: using while loop:  O(logn)
        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr


            