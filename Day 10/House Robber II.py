class Solution:
   def rob(self, nums: List[int]) -> int:
       if len(nums) == 1:
           return nums[0]
       includeLast = nums[1:]
       notLast = nums[:-1]
       maxLast = 0
       prev_rob = 0
       for num in includeLast:
           temp = max(maxLast, prev_rob + num)
           prev_rob = maxLast
           maxLast = temp
       maxNotLast = 0
       prev_rob = 0
       for num in notLast:
           temp = max(maxNotLast, prev_rob + num)
           prev_rob = maxNotLast
           maxNotLast = temp
       return max(maxNotLast, maxLast)
