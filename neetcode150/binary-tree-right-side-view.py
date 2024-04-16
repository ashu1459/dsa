# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            levelVisited = False
            for i in range(len(queue)):
                node = queue.pop(0)

                if not levelVisited:
                    res.append(node.val)
                    levelVisited = True

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return res

        