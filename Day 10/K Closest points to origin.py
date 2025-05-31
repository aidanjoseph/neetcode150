import heapq
class Solution:
   def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       #kidna peaked at topics even though shoulda
       #thoughts
       '''
       before peaked
       intiaily thoughts, i mean just calculate distance for points and
       have to sort them
       curious if i can use ad dictioanry where the distance is the
       key, and i wonder if that lets me, idk lemme try
       nope can't


       '''
       heap = []
      
       for (x, y) in points:
           dist = -(x*x + y*y)
           if len(heap) == k:
               heapq.heappushpop(heap, (dist, x, y))
           else:
               heapq.heappush(heap, (dist, x, y))
      
       return [(x,y) for (dist,x, y) in heap]
