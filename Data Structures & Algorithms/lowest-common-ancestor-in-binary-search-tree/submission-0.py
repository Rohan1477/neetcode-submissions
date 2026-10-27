# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # def dfs(root):
        #     if not root:
        #         return
            
        #     dfs(root.left)
        #     dfs(root.right)

        res = root
        while root:
            if (p.val < root.val and q.val < root.val):
                root = root.left
            
            elif (p.val > root.val and q.val > root.val):
                root = root.right

            else:
                res = root
                break

        return root

            
            
        
