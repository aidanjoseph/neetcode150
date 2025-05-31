class Solution:
   def twoSum(self, numbers: List[int], target: int) -> List[int]:
       #thoughts
       #essentially loop through and call binary search to find complement
       #would that be n log n tho?, idk lets see
       #if its sorted can i just binary search on each element basically?
       #ess
       # def binarySearch(numbers, target, start, finish):
       #     begin = start
       #     end = finish
       #     while (begin <= end):
       #         mid = begin + (end-begin)//2
       #         if numbers[mid] == target:
       #             return mid
       #         elif numbers[mid] < target:
       #             begin = mid + 1
       #         else:
       #             end = mid - 1
       #     return 'Not here'
       # a = len(numbers)
       # for i in range(len(numbers)):
       #     result = binarySearch(numbers, target - numbers[i], i + 1, a-1)
       #     if isinstance(result, str):
       #         continue
       #     else:
       #         return [i + 1, result + 1]
       left = 0
       right = len(numbers) - 1
       if (left + right == target):
           return [1, right + 1]
       while (left < right):
           sum = numbers[left] + numbers[right]
           if (sum == target):
               return [left + 1, right + 1]
           if (sum < target):
               left += 1
           else:
               right -= 1
