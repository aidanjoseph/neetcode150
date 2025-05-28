class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
       #Thoughts
       '''
       Could use a hashmap?
       1. First create our map, freq map?
       2. Then for each key check if there exists an element + or - of it
       if i just do want direction then avoid double counting
       '''
       # nums = set(nums)
       # table = {}
       # maxVal = 0
       # for num in nums:
       #     x = table.get(num - 1, 0)
       #     y = table.get(num + 1, 0)
       #     val = x + y + 1
       #     table[num - x] = val
       #     table[num + y] = val
       #     maxVal = max(maxVal, val)
       # return maxVal
       nums = set(nums)
       longest = 0
       for num in nums:
           if (num - 1) not in nums:
               length = 0
               while (num + length) in nums:
                   length += 1
               longest = max(length, longest)
       return longest
