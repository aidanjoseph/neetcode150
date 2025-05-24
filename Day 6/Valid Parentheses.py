class Solution:
   def isValid(self, s: str) -> bool:
       #thoughts
       '''
       kinda just looks like a stack


       '''
       stack = []
       for char in s:
           if char == "(" or char == "[" or char == "{":
               stack.append(char)
           if char == ")":
               if len(stack) == 0:
                   return False
               if stack[-1] == "(":
                   stack.pop()
               else:
                   return False
           elif char == "]":
               if len(stack) == 0:
                   return False
               if stack[-1] == "[":
                   stack.pop()
               else:
                   return False
           elif char == "}":
               if len(stack) == 0:
                   return False
               if stack[-1] == "{":
                   stack.pop()
               else:
                   return False
       if len(stack) != 0:
           return False
       return True


