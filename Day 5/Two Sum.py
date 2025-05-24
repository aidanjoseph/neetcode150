class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       i = 0
       for num in nums:
           complement = target - num
           if complement in seen:
               return [seen[complement],i]
           else:
               seen[num] = i
           i += 1
