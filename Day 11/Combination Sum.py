class Solution:
   def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       #Thoughts
       #just do all m combs and ad to it
      
       #can't lie im. fried had no idea
       res = []


       def dfs(i,curr,total):
           if total == target:
               res.append(curr.copy())
               return


           if i>= len(candidates) or total>target:
               return


          
           curr.append(candidates[i])
           dfs(i,curr,total + candidates[i])
           curr.pop()
           dfs(i+1,curr,total)


       dfs(0,[],0)
       return res 

