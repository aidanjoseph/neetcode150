# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def maxDepth(self, root: Optional[TreeNode]) -> int:
       #Thoughts
       '''
       Just screams classic recursion to me
       base case is if root is null then return 0
       otherwise just add root.left + root.right basically + 1 which is the
       current level, bfs type search i think
       '''
       if root is None:
           return 0
       return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
  
