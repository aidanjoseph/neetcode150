# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       #Thoughts
       #doesn't seem that hard?
       #Need to Save n -1, and n +1
       #also remember 2 edge cases where n is the head or tail


       #Handle n = 1
       # if n == 1:
       #     curr = head.next
       #     head.next = None
       #     return curr
       # toRemove = head
       # counter = 1
       # prev = head
       # while counter != n:
       #     prev = toRemove
       #     toRemove = toRemove.next
       #     counter += 1
       # toSave = toRemove.next
       # toRemove.next = None
       # prev.next = toSave
       # return head


       #erm above codes removes k from the frnot no back ,read question wrong initially
       #essentially use two pointer
       #distance between them is n, so when u reach end the distance away from end is n
       res = ListNode(0, head)
       dummy = res


       for _ in range(n):
           head = head.next
      
       while head:
           head = head.next
           dummy = dummy.next
      
       dummy.next = dummy.next.next


       return res.next
