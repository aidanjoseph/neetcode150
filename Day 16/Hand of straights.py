class Solution:
   def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
       #thoughts
       #maybe can just use some math trickshere
       if len(hand) % groupSize != 0:
           return False
       #thers an n log n one via sorting
       hand.sort()
       def findStraight(hand, groupSize, i, n):
           next_val = hand[i] + 1
           hand[i] = -1 #used
           count = 1
           i += 1
           while i < n and count < groupSize:
               if hand[i] == next_val:
                   next_val = hand[i] + 1
                   hand[i] = -1
                   count += 1
               i += 1
           return count == groupSize
       n = len(hand)
       for i in range(n):
           if hand[i] >= 0:
               if not findStraight(hand, groupSize, i, n):
                   return False
       return True
