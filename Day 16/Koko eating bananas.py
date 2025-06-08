class Solution:
   def minEatingSpeed(self, piles: List[int], h: int) -> int:
       #thougths
       '''
       wonder if can do a binary search on the k
       but how to pick a starting value, i suppose max would be the max of piles
       and min would just have to default to 1, and we start at the mid?
       #but if we do find something we have to check belo it
       #onsider example 1, k = 5 also has h = 8
       # '''
       # end = max(piles)
       # begin = 1
       # def calculateHours(piles, k):
       #     curr = 0
       #     hours = 0
       #     for pile in piles:
       #         curr = pile
       #         while curr > 0:
       #             curr -= k
       #             hours += 1
       #     return hours
       # while begin < end:
       #     mid = begin + (end-begin)//2
       #     hours = calculateHours(piles, mid)
       #     if hours > h:
       #         begin = begin + 1
       #     else:
       #         end = mid
       # return begin
       def check(piles, h, mid):
           ans = 0
           for pile in piles:
               ans += pile // mid
               if pile % mid != 0:
                   ans += 1
           return 1 if ans <= h else 0


       low = 1
       high = max(piles)


       while low < high:
           mid = (low + high) >> 1
           if check(piles, h, mid) == 1:
               high = mid
           else:
               low = mid + 1
              
       return low

