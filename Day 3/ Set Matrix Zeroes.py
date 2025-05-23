class Solution:
   def setZeroes(self, matrix: List[List[int]]) -> None:
       """
       Do not return anything, modify matrix in-place instead.
       """
       #Thoughts
       """
       Trivially, could just double for loop over whole thing
       have arrray for i index and j index, then iterate again to reset      everything
       just gonna do triviak for now
       """
       iMatrix = {}
       jMatrix = {}
       for i in range(len(matrix)):
           for j in range(len(matrix[i])):
               if matrix[i][j] == 0:
                   iMatrix[i] = 0
                   jMatrix[j] = 0
       for i in range(len(matrix)):
           for j in range(len(matrix[i])):
               if i in iMatrix or j in jMatrix:
                   matrix[i][j] = 0
