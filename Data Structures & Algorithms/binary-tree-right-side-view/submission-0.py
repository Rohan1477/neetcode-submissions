# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = []
        

        def bfs():

            queue = collections.deque()

            if root:
                queue.append(root)
            
            #level = 0
            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                self.res.append(node.val)
                #level++
        
        bfs()

        return self.res

                

