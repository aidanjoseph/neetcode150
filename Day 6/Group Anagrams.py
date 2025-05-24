class Solution:
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       sortedMap = {}
       for i in range(len(strs)):
           sorted_chars = sorted(strs[i])
           sorted_word = "".join(sorted_chars)
           if sorted_word in sortedMap:
               sortedMap[sorted_word].append(strs[i])
           else:
               sortedMap[sorted_word] = [strs[i]]
       toReturn = []
       for key in sortedMap:
           toReturn.append(sortedMap[key])
       return toReturn
