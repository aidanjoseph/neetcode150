# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       #Thoughts
       '''
       just
       '''
       if root is None:
           return None
       self.swap(root)
       self.invertTree(root.left)
       self.invertTree(root.right)
       return root


   def swap(self, root):
       temp = root.left
       root.left = root.right
       root.right = temp
