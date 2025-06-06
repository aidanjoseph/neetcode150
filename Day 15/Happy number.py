class Solution:
   def isHappy(self, n: int) -> bool:
       if n == 1:
           return True
       seen = {}
       seen[n] = "here"
       def calculHappy(n):
           stringN = str(n)
           prod = 0
           for char in stringN:
               prod += int(char) * int(char)
           return prod
       curr = calculHappy(n)
       while curr not in seen:
           seen[curr] = "here"
           if curr == 1:
               return True
           curr = calculHappy(curr)
       return False
      
