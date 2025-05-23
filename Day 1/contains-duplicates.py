class Solution:
   def containsDuplicate(self, nums: List[int]) -> bool:
        #Thoughts
       '''
       Use hashmap to store integers
       so can just iterate over array linearly
       check if curr in hashmap
       '''




       #Solution
       '''
       Hashmap to store nums
       for loop to iterate over array
       '''
       duplicateTracker = {}
       for num in nums:
           if num in duplicateTracker:
               return True
           else:
               duplicateTracker[num] = "here"
       return False
