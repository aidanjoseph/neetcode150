class Solution:
   def findKthLargest(self, nums: List[int], k: int) -> int:
       #idk just sounds like a heap sorta
       #prob not just heapify the nunms as thats a n log n op i thnk?
       #create our own empty heap
       #and populate it with nums
       heap = []
       for num in nums:
           if len(heap) == k:
               heapq.heappushpop(heap, num)
           else:
               heapq.heappush(heap, num)
       for i in range(len(heap)):
           heap[i] = -heap[i]
       heapq.heapify(heap)
       counter = 0
       while counter != k:
           counter += 1
           ans = heapq.heappop(heap)
       return -ans


       # a nicer version of what is houlda done
       # min_heap = []


       # for num in nums:
       #     heapq.heappush(min_heap, num)
       #     if len(min_heap) > k:
       #         heapq.heappop(min_heap)


       # return min_heap[0]
      
