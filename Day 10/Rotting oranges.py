class Solution:
   def orangesRotting(self, grid: List[List[int]]) -> int:
       #thoughts
       #sounds very similar to that walls and gates problem or whaterv
       #i thinkw e wanna start at the rotten ones
       #and run a bfs from them
       #and each time we do we increment, by 1
       #only annoying part is we have to account for the edge case where
       #there is not a rotten apple
       
       rows, cols = len(grid), len(grid[0])
       def checkAllRotten():
           allRotten = True
           for r in range(rows):
               for c in range(cols):
                   if grid[r][c] == 1:
                       return False
           return True
       if checkAllRotten():
           return 0
       visit = set()
       q = deque()
       def rot(r,c):
           if (r < 0 or r == rows or c < 0 or c== cols):
                return
           if (r, c) in visit or grid[r][c] == 0:
               return
           visit.add((r,c))
           q.append([r,c])
    
    
       for r in range(rows):
           for c in range(cols):
               if grid[r][c] == 2:
                   q.append([r,c])
                   visit.add((r,c))
       time = 0
       while q:
           for i in range(len(q)):
               r,c = q.popleft()
               grid[r][c] = dist
               rot(r+1, c)
               rot(r-1,c)
               rot(r,c+1)
               rot(r,c-1)
           time += 1
       if not checkAllRotten():
           return -1
       else:
           return time - 1


