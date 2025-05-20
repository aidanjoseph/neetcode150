# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       #Thoughts
       '''
       not as intuitive as i thoguht (prob still easy but jumped the gun)
       given a list [1,2]
       would start with 1 as curr and prev as None
       then would do set its next as prev and in that loop curr = curr.next
       but before we reassign pointer
       so like 1, 2
       prev = None
       curr = 1
       temp = curr.next
       curr.next = prev
       curr = temp
       '''
       prev = None
       curr = head
       if (curr is None):
           return head
       while (curr != None):
           #store the next value
           temp = curr.next #temp = 2, #temp = None


           #reassign the current next
           curr.next = prev #curr.next = None, #curr.next = 1
           prev = curr #prev = 1, #prev = 2
          
           curr = temp #curr = 2, #curr = None
       return prev
