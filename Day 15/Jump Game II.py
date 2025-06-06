class Solution:
   def jump(self, nums: List[int]) -> int:
       #thoughts
       '''
       what if i just caclualte hte length of the array
       and hten for each index
       if the curesnt sum till ther eis greater than i can return that count?
       maybe
       '''
       #[2,3,1,1,4]
       #curr_largest is 2, and check if next is >=
       #curr_largset is 3, next 
       near = far = jumps = 0
       while far < len(nums) - 1:
           farthest = 0
           for i in range(near, far + 1):
               farthest = max(farthest, i + nums[i])
           near = far + 1
           far = farthest
           jumps += 1
       return jumps 
      



