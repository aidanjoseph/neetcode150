class Solution:
   def singleNumber(self, nums: List[int]) -> int:
       #Thoughts
       #O(1)
       #********
       '''
       & is bitwise and,
       | is bitwise or,
       ^ is bitwise xor,
       >> is bitwise right shift,
       << is bitwise left shift,
       ~ is bitwise complement
       '''
       #print(9 & 3) #1001 and 0011, false false false true 0001
       #treu fale true rue 1011, xor true false true false 1010
       #print(5>>2) #1100
       #100 001, --> 101,
       #01 10 --> 011
       # ---> 011
       # --> 011
       #100 001 010 001 010 -->
       # 101 010 001 010 --
       # 111 001 010
       # 110 010
       # 100
       if len(nums) == 1:
           return nums[0]
       curr = nums[0]
       for i in range(1, len(nums)):
           curr = curr ^ nums[i]
       return curr


