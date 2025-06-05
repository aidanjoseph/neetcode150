class Solution:
   def missingNumber(self, nums: List[int]) -> int:
       n = len(nums)
       inclusiveSum = 1
       for i in range(1,n+1):
           inclusiveSum *= i
       exclusiveSum = 1
       zeroExists = False
       for num in nums:
           if num != 0:
               exclusiveSum *= num
           else:
               zeroExists = True
       if not zeroExists:
           return 0
       elif exclusiveSum == inclusiveSum:
           return 1
       else:
           return inclusiveSum//exclusiveSum
       #bitwise operation approach, nice to know used xor
       #xor with same number is 0
       #0 xor some num is that num
       #  n = len(nums)
       # ans = 0
       # for i in range(1, n + 1):
       #     ans ^= i
       # for num in nums:
       #     ans ^= num
       # return ans


      
