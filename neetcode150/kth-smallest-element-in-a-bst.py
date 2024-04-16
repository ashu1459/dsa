# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    elem = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Solution-1: Without recursion
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right

    #     # Solution-2: use in-order traversal
    #     self.dfs(root, k)

    #     return self.elem

    # def dfs(self, node, k):
    #     if not node:
    #         return k

    #     if node.left:
    #         k = self.dfs(node.left, k)

    #     k -= 1
    #     if k == 0:
    #         self.elem = node.val
    #         return 0

    #     if node.right:
    #         k = self.dfs(node.right, k)
        
    #     return k