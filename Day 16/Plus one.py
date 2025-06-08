class Solution:
   def plusOne(self, digits: List[int]) -> List[int]:
       #just kinda tedious
       #loop backwards check if we need to carry over anything, but it''
       #just be a zero
       digits[-1] += 1
       if digits[-1] < 10:
           return digits
       digits[-1] = 0
       if len(digits) == 1:
           digits.insert(0,1)
           return digits
       addToEnd = False
       for i in range(len(digits)-2,-1,-1):
           digits[i] += 1
           if digits[i] == 10:
               digits[i] = 0
               if i == 0:
                   addToEnd = True
           else:
               break
       if addToEnd:
           digits.insert(0,1)
       return digits
