class Solution:
   def countBits(self, n: int) -> List[int]:
       #thoughts
       '''
       use sum kinda of bit operation


       '''
       #my solution
       res = []
       def nums1s(n):
           if n == 0:
               return 0
           return (n & 1) + nums1s(n>>1)
       for i in range(n+1):
           res.append(nums1s(i))
       return res
       #optimal
       # ans = [0] * (n + 1)
       # for i in range(1, n + 1):
       #     ans[i] = ans[i >> 1] + (i & 1)
       # return ans


