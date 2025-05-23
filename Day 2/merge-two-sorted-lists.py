# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       #Thoughts
       '''
       just a while loop with guard about both being next's being none or head
       if greater
       '''
       curr1 = list1
       curr2 = list2
       toReturn = curr1 #Default as list1 head
       if curr1 and curr2:
           if curr1.val > curr2.val:
               toReturn = curr2
               curr2 = curr2.next
           else:
               curr1 = curr1.next
       elif curr1 and not curr2:
           return curr1
       else:
           return curr2
       toReturnCurr = toReturn
       while (curr1 or curr2):
           if curr1 and curr2:
               if curr1.val > curr2.val:
                   toReturnCurr.next = curr2
                   toReturnCurr = toReturnCurr.next
                   curr2 = curr2.next
               else:
                   toReturnCurr.next = curr1
                   toReturnCurr = toReturnCurr.next
                   curr1 = curr1.next
           elif curr1 and not curr2:
               toReturnCurr.next = curr1
               toReturnCurr = toReturnCurr.next
               curr1 = curr1.next
           elif curr2 and not curr1: 
               toReturnCurr.next = curr2
               toReturnCurr = toReturnCurr.next
               curr2 = curr2.next
       return toReturn
          
