class Solution:
   def isPalindrome(self, s: str) -> bool:
       #Thoughts
       '''
       Two Pointer Solution?
       just go from both ends
       i = 0
       j = len(s) - 1
       loop guard i < j
       '''
       i = 0
       j = len(s) - 1
       while (i <= j):
           if s[i].isalnum() and s[j].isalnum():
               if s[i].lower() != s[j].lower():
                   return False
               else:
                   i += 1
                   j -= 1
           else:
               if not s[i].isalnum():
                   i+=1
               elif not s[j].isalnum():
                   j-=1
       return True
