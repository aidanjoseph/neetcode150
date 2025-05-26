class Solution:
   def rob(self, nums: List[int]) -> int:
       #Thoughts
       '''
       Is it not just, do u make more starting at index 1 or 0
       cuz u have to skip 2 every time cuz of the adjancey issue
        i think?, thought of a counter but just supports oht
       [1,100000,2,5,12041203748]
       not as simople as index 0 or 1,
       cuz here best is index 1, then index 4
       '''
       n = len(nums)
       if n is 1:
           return nums[0]
       dp = [0] * n
       dp[0] = nums[0]
       dp[1] = max(nums[0], nums[1])
       for i in range(2,n):
           dp[i] = max(dp[i-1], nums[i] + dp[i-2])
       return dp[-1]
       ''' O(1)
       prev_rob = max_rob = 0
       for curr_val in nums:
           temp = max(max_rob, prev_rob + cur_val)
           prev_rob = max_rob
           max_rob = temp
       return max_rob
       '''
