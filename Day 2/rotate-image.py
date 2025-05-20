class Solution:
   def rotate(self, matrix: List[List[int]]) -> None:
       """
       Do not return anything, modify matrix in-place instead.
       """
       #Thoughts
       '''
       i, j where is is outer list, i = row, j = colw
       Consider top left corner
       [0,0] becomes [0,2]
       top right Corner
       [0,2] becomes [2,2]
       bototm right corner
       [2,2] becomes [2,0]
       top left corner
       [2,0] becomes [0,0]


       Hmm
       Consider representing with a Stack
       iterate through first element of each


       Start: [1,2,3], [4,5,6], [7,8,9]
       Step 1: [3,2,1], [4,5,6], [7,8,9] Swapped [0,0] and [0,2]
       Step 2: [7,2,1], [4,5,6], [3,8,9] Swapped [0,1] and [2,1]
       Step 3: [7,4,1], [2,5,6], [3,8,9] Sapped [0,2] and [1,0]
       Step 4: [7,4,1], [6,5,2], [3,8,9]
       Step 4: Step 3: [7,4,1], [8,5,2], [9,6,3]


       '''
       def swap (matrix:  List[List[int]], pos1: [int,int], pos2: [int,int]):
           tempI = pos1[0]
           tempJ = pos1[1]
           tempValue = matrix[tempI][tempJ]
           matrix[tempI][tempJ] = matrix[pos2[0]][pos2[1]]
           matrix[pos2[0]][pos2[1]] = tempValue
       top = 0
       bottom = len(matrix) - 1
       left = 0
       right = len(matrix[0]) - 1
       while (left < right):
           for i in range(right - left):
               top = left
               bottom = right
               swap(matrix, [top,left + i], [bottom - i,left])
               swap(matrix, [bottom - i,left], [bottom,right - i])
               swap(matrix, [bottom, right -i], [top+i, right])
           right -= 1
           left += 1
