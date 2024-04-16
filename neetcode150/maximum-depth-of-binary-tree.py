# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Solution-1: DFS with recursion
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Solution-2: BFS - using iterative approach with deque
        # level = 0
        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1

        # return level

        # Solution-3: DFS - using iterative approach with stack
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res


