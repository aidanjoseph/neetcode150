class Solution:
   def climbStairs(self, n: int) -> int:
       #Thoughts
       '''
       Consider n = 4
       #Base case: always trivilally a solution
       1 step + 1 step + 1 step + 1 step
       #Second Base Case: If n is even then we have a form with all 2's
       2 step + 2 step
       #Third Case: mix of 2's and 1's
       2 step + 1 step + 1 step
       1 step + 2 step + 1 step
       1 step + 1 step + 2 step
       n = 4, 5


       5


       Needed to watch video im clipped
       '''

       #WATCHED VIDEO FOR THIS APPROACH
       one = 1
       two = 1
       for i in range(n - 1):
           temp = one
           one = one + two
           two = temp
       return one
