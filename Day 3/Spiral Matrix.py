class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       #Thoughts
       '''
       [0,0], [0,1], [0,2], [1,2], [2,2], [2,1], [2,0], [1,0],[1,1]


       [0,0], [0,1], [0,2], [0,3], [1,3], [2,3], [2,2], [2,1], [2,0], [1,0],
       [1,1], [1,2], [1,3]
       '''
       res = []
       left, right = 0, len(matrix[0])
       top, bottom = 0, len(matrix)
       while left < right and top < bottom:
           #get every i in top row
           for i in range(left, right):
               res.append(matrix[top][i])
           top += 1


           #get every i in right col
           for i in range(top, bottom):
               res.append(matrix[i][right-1])
           right -= 1


           #for single cols or single rows
           if not (left < right and top < bottom):
               break
           #left -1 for inclusive, -1 for decrementing
           for i in range (right -1, left-1, -1):
               res.append(matrix[bottom-1][i])
           bottom -= 1


           #get every in in left col
           for i in range (bottom-1, top-1, -1):
               res.append(matrix[i][left])
           left += 1
       return res


