class Solution:
   def canJump(self, nums: List[int]) -> bool:
       #thoughts
       '''
       start from end,
       kinda like accumulation
       [2,3,1,1,4]
       start at 4, index 3 needs to be >= 1
       index 2 >= 2, index 1 >= 3
       our goal can be shifted if the one before is 1
       [2,3,1,1,4]
       baially since have 1 shift our goal to index 3
       since we have another one
       shifted our goal to index 2
       now find a 3, so we can def make to index 2, so shiftgoal over again


       '''
       goal = len(nums) - 1
       for i in range(len(nums)-1, -1, -1):
           if nums[i] >= goal - i:
               goal = i
       if goal == 0:
           return True
       return False




