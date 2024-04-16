# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # using extra space
        # n = TreeNode(root.val)
        # n.left = self.invertTree(root.right)
        # n.right = self.invertTree(root.left)
        # return n

        # In-Place - swap the children
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)

        return root