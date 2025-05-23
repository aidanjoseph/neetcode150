class Solution:
   def search(self, nums: List[int], target: int) -> int:
       #thoughts basic binary search
       begin = 0
       end = len(nums)-1
       mid = int((begin + end) / 2 )
       while (begin <= end):
           if nums[mid] == target:
               return mid
           elif nums[mid] > target:
               end = mid - 1
               mid = int((begin + end)/2)
           else:
               begin = mid + 1
               mid = int((begin + end)/2)
       return -1
