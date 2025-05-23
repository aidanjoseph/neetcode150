class MinStack:


   def __init__(self):
       self.minStack = []
       self.minVal = None
       self.length = 0
       self.innerStack = []
       self.lengthInner = 0
      


   def push(self, val: int) -> None:
       self.minStack.append(val)
       if self.minVal is not None:
           if val <= self.minVal:
               self.minVal = val
               self.innerStack.append(val)
               self.lengthInner += 1
       else:
           self.minVal = val
           self.innerStack.append(val)
           self.lengthInner += 1
       self.length += 1
      


   def pop(self) -> None:
       currVal = self.minStack.pop()
       self.length -= 1
       if currVal == self.minVal:
           self.innerStack.pop()
           self.lengthInner -= 1
           if self.lengthInner == 0:
               self.minVal = None
           else:
               self.minVal = self.innerStack[self.lengthInner-1]
          




      


   def top(self) -> int:
       return self.minStack[self.length-1]
      


   def getMin(self) -> int:
       return self.minVal
      




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
