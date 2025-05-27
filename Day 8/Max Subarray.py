class Solution:
   def maxSubArray(self, nums: List[int]) -> int:
       #thoughts
       '''
       prob can just itereate through array once
       have curr_sum and max_sum
       consider
       [-2,1,-3,4,-1,2,1,-5,4]
       max_sum
       '''
       maxSub = nums[0]
       currSum = 0
       for n in nums:
           if currSum < 0:
               currSum = 0
           currSum += n
           maxSub = max(maxSub, currSum)
       return maxSub
