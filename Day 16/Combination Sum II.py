class Solution:
   def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       res = []
       ds = []
       candidates.sort()
       def findCombination(ind, target):
           if target == 0:
               res.append(ds[:])
               return
           for i in range(ind, len(candidates)):
               if i > ind and candidates[i] == candidates[i - 1]:
                   continue
               if candidates[i] > target:
                   break
               ds.append(candidates[i])
               findCombination(i + 1, target - candidates[i])
               ds.pop()
       findCombination(0, target)
       return res
