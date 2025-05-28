# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
   def reorderList(self, head: Optional[ListNode]) -> None:
       """
       Do not return anything, modify head in-place instead.
       """
       #what if i use a double ended queue
       #popleft, pop right
       #just add to the deque linearly
       # q = deque
       # curr = head
       # while curr:
       #     q.append(curr)
       #     curr = curr.next
       # #Now we want algorithm
       # #Pop L0, initially
       # #in loop, popright, store it as next of L0, make LN curr then popleft
       # #might need a tracker to see which one we pop
       # left = False
       # curr = q.popleft()
       # toConnect = 1239
       # while q:
       #     if left:
       #         toConnect = q.popleft()
       #     else:
       #         toConnect = q.popright()
       #     curr.next = toConnect
       #     curr = toConnect
       #can't deque.append a listNode, ....
       fastCurr = head
       slowCurr = head
       while fastCurr and fastCurr.next:
           slowCurr = slowCurr.next
           fastCurr = fastCurr.next.next
       #Now reverse second half
       curr = slowCurr.next
       slowCurr.next = None
       prev = None
       while curr:
           temp = curr.next
           curr.next = prev
           prev = curr
           curr = temp


       first = head
       second = prev
       while second:
           temp1, temp2 = first.next, second.next
           first.next, second.next = second, temp1
           first, second = temp1, temp2
