class Solution:
   def canPartition(self, nums: List[int]) -> bool:
       #thoughts
       '''
       i feel like i can just sort this and then run a two pointer on this
       n log n time soltuion
       not sure if i can do better so imma just try that
       THAT does not work
       consider [2,2,1,1]
       subests of 1,2 and 1,2 is valid but sorting and two pointe rwould not find this


       '''
       sum = 0
       for num in nums:
           sum += num
       if sum % 2 == 1:
           return False
       target = sum // 2
       possible = [False] * (target + 1)
       possible[0] = True
       for num in nums:
           for currSum in range(target, num - 1, -1):
               possible[currSum] = possible[currSum] or possible[currSum - num]
       return possible[target]


      
 
