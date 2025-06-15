class Solution:
   def findDuplicate(self, nums: List[int]) -> int:
       #thoughts
       #i mean constant space is the hard part
       #obvious natural solution is via set or hashmap and marking something as seen
       #i mgihta seen this before but lets see
       #n^2 solution, double for loop check if something - another is == 0
       #if so return that number
       # an nlog n one would be to sort but cant modify array
       #fast and slow pointers cycle, saw that
       slow, fast = 0,0
       while True:
           slow = nums[slow]
           fast = nums[nums[fast]]
           if slow == fast:
               break
       slow2 = 0
       while True:
           slow = nums[slow]
           slow2 = nums[slow2]
           if slow == slow2:
               return slow
