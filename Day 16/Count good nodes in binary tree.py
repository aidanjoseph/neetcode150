# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def goodNodes(self, root: TreeNode) -> int:
       #just do a bfs but i guess keep track of our max on left and right
       #or a dfs idk doens't matter
       goodCount = [0]
       if not root:
           return 0
       def dfs(node, currMax):
           if not node:
               return
           if node.val >= currMax:
               goodCount[0] += 1
               currMax = node.val
           dfs(node.left, currMax)
           dfs(node.right, currMax)
       dfs(root, root.val)
       return goodCount[0]
