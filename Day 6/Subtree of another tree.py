# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       #thoughts
       '''
       wanna have a check for is same tree, call on every root?
       kinda expensive, maybe don't make call unless values are equal
       '''
       def isSameTree(p, q):
           if p is None and q is None:
               return True
           elif p is None or q is None:
               return False
           elif p.val != q.val:
               return False
           return isSameTree(p.left,q.left) and isSameTree(p.right, q.right)
       def dfs(root):
           if root is None:
               return False
           if isSameTree(root, subRoot):
               return True
           return dfs(root.left) or dfs(root.right)
       return dfs(root)
