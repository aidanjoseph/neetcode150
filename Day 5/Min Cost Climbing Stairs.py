class Solution:
   def minCostClimbingStairs(self, cost: List[int]) -> int:
       #lowkey just fibnoacci but you min it or some hting
       #reverse climbing
       if len(cost) == 1:
           return cost[0]
       dp = [0] * (len(cost) + 2)
       print(dp)
       for i in range(len(cost)-1, -1, -1):
           dp[i] = cost[i] + min(dp[i+1], dp[i+2])
       return min(dp[0], dp[1])
       #for O(1) space
       '''
       cost.append(0)
       for i in range(len(cost)-3, -1, -1):
           cost[i] += min(cost[i+1], cost[i+2])
       return min(cost[0],cost[1])
       does same thing but no new array
       '''
