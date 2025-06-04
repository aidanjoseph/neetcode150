class Solution:
   def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
       a = target[0]
       b = target[1]
       c = target[2]
       newTrips = []
       for triplet in triplets:
           if triplet[0] > a:
               continue
           elif triplet[1] > b:
               continue
           elif triplet[2] > c:
               continue
           else:
               newTrips.append(triplet)
       aExists = False
       bExists = False
       cExists = False
       for triplet in newTrips:
           if a == triplet[0]:
               aExists = True
           if b == triplet[1]:
               bExists = True
           if c == triplet[2]:
               cExists = True
       if aExists and bExists and cExists:
           return True
       return False 
      

