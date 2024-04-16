# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if not root and not subRoot:
        #     return True
        # if not root:
        #     return False
        # if not subRoot:
        #     return True
        
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSame(node, subRoot):
                    return True
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False

    def isSame(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

        return False
