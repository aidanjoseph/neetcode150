class Solution:
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       #Thoughts
       '''
       Use a hashmap --> Key = num, val = frequency
       maybe a list of the hashmaps
       '''
       freq = {}
       for num in nums:
           if num in freq:
               freq[num] += 1
           else:
               freq[num] = 1
       kFreq = []
       for i in range(len(nums)):
           kFreq.append([])
       toReturn = []
       if len(toReturn) == k:
           return toReturn
       for key in freq:
           kFreq[freq[key]-1].append(key)
       for i in range(len(kFreq)-1,-1,-1):
           if kFreq[i] != []:
               for j in range(len(kFreq[i])):
                   if len(toReturn) == k:
                       return toReturn
                   else:
                       toReturn.append(kFreq[i][j])
       return toReturn