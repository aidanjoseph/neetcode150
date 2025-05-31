class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
       #thoughts
       '''
       i mean its like a sliding window right
       i just move forward
       have a hashmap where i last seen a character
        '''
       i = 0
       last_Seen = {}
       maxLength = 0
       for j, char in enumerate(s):
           if char in last_Seen and last_Seen[char] >= i:
               i = last_Seen[char] + 1
           maxLength = max(j - i + 1, maxLength)
           last_Seen[char] = j
       return maxLength


