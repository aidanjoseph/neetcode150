class Solution:
   def maxProfit(self, prices: List[int]) -> int:
       #Thoughts
       '''
       Use a two pointer solution
       i --> start arary
       j --> maybe not end of array but rather, i + 1
       max_diff --> max difference
       curr_diff --> current diff, if greater than max, reset max_diff
       move


       Example algorithm:
       [7,1,5,3,6,4]
       prices[i] = 7, prices[j] = 1
       diff = 6, whcih is not not good
       since prices[j] > prices[i] lets increment both by 1
       now prices[i] = 1, prices[j] = 5, get -4, nice
       again lets check if prices[j] > prices[i], but not so let's increment j
       and repeat
       '''
       i = 0
       j = i + 1
       max_diff = 0
       curr_diff = 0
       while (j < len(prices)):
           curr_diff = prices[i] - prices[j]
           if curr_diff < max_diff:
               max_diff = curr_diff
           if prices[i] > prices[j]:
               i = j
               j+=1
           else:
               j+=1
       return int(math.fabs(max_diff))

