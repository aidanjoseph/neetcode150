class Solution:
   def islandsAndTreasure(self, grid: List[List[int]]) -> None:
       #thoguhts
       '''
       Intuition
       We do a bfs on the graph
       and we can just direclty mark the distance without worryitng. ithink
       cuz if we find a value > 0 and < inf, we can just
       use that number + our curr distance to get a distance,
       and if our counter exceeds that, we can just mark down
       the tile as that distance
       essentially a bfs on each inf tile i thnk
       or run bfs on the gates which is what neetcode says
       '''
       rows, cols = len(grid), len(grid[0])
       visit = set()
       q = deque()
       def addRoom(r,c):
           if (r < 0 or r == rows or c < 0 or c== cols):
               return
           if (r, c) in visit or grid[r][c] == -1:
               return
           visit.add((r,c))
           q.append([r,c])
      
      
       for r in range(rows):
           for c in range(cols):
               if grid[r][c] == 0:
                   q.append([r,c])
                   visit.add((r,c))
       dist = 0
       while q:
           for i in range(len(q)):
               r,c = q.popleft()
               grid[r][c] = dist
               addRoom(r+1, c)
               addRoom(r-1,c)
               addRoom(r,c+1)
               addRoom(r,c-1)
           dist += 1
