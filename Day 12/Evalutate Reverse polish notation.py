class Solution:
   def evalRPN(self, tokens: List[str]) -> int:
       #thoughts
       '''
       did this in a 2110 assignement
       kinda revsiited it to look at what id id so kinda cheated dbut idk
       i know its a stack imeplement but lets see if i can actually do it
       '''
       stack = []
       for token in tokens:
           if token == "+":
               stack.append(stack.pop() + stack.pop())
           elif token == "-":
               right = stack.pop()
               left = stack.pop()
               stack.append(left-right)
           elif token == "*":
               stack.append(stack.pop() * stack.pop())
           elif token == "/":
               right = stack.pop()
               left = stack.pop()
               stack.append(int(left/right))
           else:
               stack.append(int(token))
       return stack[0]


      
