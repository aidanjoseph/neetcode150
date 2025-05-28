# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
   def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
       #bst invarian
       #if both greater than a root, dfs on the right, vise versa too
       # if one les than and one greater then that is the LCA
       #keep dfs until u find where one greater and one les
       #my solution
       if p is root or q is root:
           return root
       if p.val < root.val and root.val < q.val:
           return root
       elif q.val < root.val and root.val < p.val:
           return root
       if p.val > root.val and q.val > root.val:
           return self.lowestCommonAncestor(root.right, p, q)
       else:
           return self.lowestCommonAncestor(root.left, p, q)
       #an iterative version
       '''
       while root:
           if p.val > root.val and q.val > root.val:
               root = root.right
           elif p.val < root.val and q.val < root.val:
               root = root.left
           else:
               return root
       '''
