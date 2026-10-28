# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def dfs(root, maxP):
            if not root:
                return
            
            if root.val >= maxP:
                self.count +=1
                maxP = root.val

            dfs(root.left, maxP)
            dfs(root.right, maxP)


        dfs(root, -101)

        return self.count
