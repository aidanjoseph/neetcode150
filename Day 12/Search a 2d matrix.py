class Solution:
   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       #thoughts
       '''
       just binary search ecah row or column?
       '''
       #m log n
       # def binarySearch(array, target):
       #     begin = 0
       #     end = len(array) - 1
       #     while (begin <= end):
       #         mid = (begin) + (end-begin)//2
       #         if array[mid] == target:
       #             return True
       #         elif array[mid] < target:
       #             begin = mid + 1
       #         else:
       #             end = mid -1
       #     return False
       # for r in range(len(matrix)):
       #     if (binarySearch(matrix[r], target)):
       #         return True
       # return False
       #log m * n
       if not matrix or not matrix[0]:
           return False
       row, col = len(matrix), len(matrix[0])
       left, right = 0, row * col - 1
       while left <= right:
           mid = (left + right) // 2
           middle = matrix[mid // col][mid % col]
           if middle == target:
               return True
           elif middle < target:
               left = mid + 1
           else:
               right = mid - 1
       return False
      
