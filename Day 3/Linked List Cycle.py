# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
   def hasCycle(self, head: Optional[ListNode]) -> bool:
       #Thoughts
       '''
       Just use a hashmap to keep track of visited nodes?
       otherwise just iteraete through linearlty
       pretty trivial
       what about O(1) space complexity though?
       uh not sure if allowed to change values but this is a pretty easy way
       '''
       curr = head
       while (curr):
           if curr.val == "seen":
               return True
           else:
               curr.val = "seen"
               curr = curr.next
       return False
       """
       fast = head
       slow = head
       while fast and fast.next:
           fast = fast.next.next
           slow = fast.next
           if slow == fast:
               return True
       return False
       """
