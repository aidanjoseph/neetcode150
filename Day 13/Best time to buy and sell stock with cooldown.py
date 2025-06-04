class Solution:
   def maxProfit(self, prices: List[int]) -> int:
       #thoughts
       '''
       i maean its like that one dp question where its like a min or something
       working backwards helps
       [1,2,3,0,2]
       between 0 and 2, you wanna buy on 0 and sell on 2
       '''
       if len(prices) == 1:
           return 0
       dp = {} #key = (i, buying), val maxprofit
       def dfs(i, buying):
           if i >= len(prices):
               return 0
