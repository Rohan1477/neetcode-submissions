# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(root):
            if not root:
                return 0

            return 1 + max(height(root.left), height(root.right))

        def diameter(root):
            height_l = height(root.left)
            height_r = height(root.right)

            return (height_l + height_r)

        self.max_d = 0

        def dfs(node):
            if not node:
                return
            self.max_d = max(self.max_d, diameter(node))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.max_d

         