class Solution:
   def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
       # nums.sort()
       # res = []
       # subset = []




       # def create_subset(i):
       #     if i == len(nums):
       #         res.append(subset[:])
       #         return
        
       #     subset.append(nums[i])
       #     create_subset(i+1)




       #     subset.pop()
       #     create_subset(i+1)




       # create_subset(0)
       # return res


       nums.sort()
       res = [[]]
      
       for num in nums:
           new_subsets = []
           for subset in res:
               new_set = subset + [num]
               if new_set not in res:
                   new_subsets.append(new_set)
           res.extend(new_subsets)
      
       return res
