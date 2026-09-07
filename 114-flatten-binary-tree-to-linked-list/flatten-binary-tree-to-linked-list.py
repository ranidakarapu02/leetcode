# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
     
    
        self.prev = None

        def dfs(node):
            if not node:
                return

            # First right
            dfs(node.right)

            # Then left
            dfs(node.left)

            # Connect current node
            node.right = self.prev
            node.left = None

            # Update previous
            self.prev = node

        dfs(root)