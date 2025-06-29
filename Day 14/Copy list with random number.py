"""
# Definition for a Node.
class Node:
   def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
       self.val = int(x)
       self.next = next
       self.random = random
"""


class Solution:
   def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       nodeDict = {None:None}
       curr = head
       while curr:
           nodeDict[curr] = Node(curr.val)
           curr = curr.next
       curr = head
       while curr:
           copy = nodeDict[curr]
           copy.next = nodeDict[curr.next]
           copy.random = nodeDict[curr.random]
           curr = curr.next
       return nodeDict[head]

