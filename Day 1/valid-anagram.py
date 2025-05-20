class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
       #Thoughts:
       '''
       Just iterate over the strings fully,
       use a dictionary to track letters
       Hm
       Essentially keys would be letters
       and values would be the number of instances
       could do a thing where i use one hashmap
       if in s then +1
       if in t then -1
       if all 0 then we good basically cuz everything cancels out
       '''
       if len(s) != len(t):
           return False
       letterCounter = {}
       for i in range(len(s)):
           if s[i] in letterCounter:
               letterCounter[s[i]] += 1
           else:
               letterCounter[s[i]] = 1
           if t[i] in letterCounter:
               letterCounter[t[i]] -= 1
           else:
               letterCounter[t[i]] = -1
       for key in letterCounter:
           if letterCounter[key] != 0:
               return False
       return True
