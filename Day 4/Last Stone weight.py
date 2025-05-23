import heapq
class Solution:
   def lastStoneWeight(self, stones: List[int]) -> int:
       #Thoughts
       '''
       Before hint thoughts:
           make a max function for second highest
           or use a sorting algorithm but n log n
       lowkey looked at the hint
       '''
       if stones is None:
           return 0
       if len(stones) == 1:
           return stones[0]
       stones = [-stone for stone in stones]
       heapq.heapify(stones)
       curr = -heapq.heappop(stones)
       while (len(stones) > 0):
           curr = curr - -heapq.heappop(stones)
           curr = -heapq.heappushpop(stones, -curr)
       return int(math.fabs(curr))
