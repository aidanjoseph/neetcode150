# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       #thoughts
       '''
       root's awlays gonna be there
       if there exists a right on that level, that's the only seen one
       if not then the next rightmost one on that level
       kinda like a modified bfs
       '''
       res = []
       if not root:
           return res
       q = collections.deque()
       q.append(root)
       while q:
           rightMost = None
           i = 0
           count = len(q)
           for _ in range(len(q)):
               i += 1
               node = q.popleft()
               if node.left:
                   q.append(node.left)
               if node.right:
                   q.append(node.right)
               if i == count:
                   rightMost = node
           res.append(rightMost.val)
       return res
