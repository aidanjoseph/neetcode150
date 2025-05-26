class Solution:
   def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       #thoughts
       '''
       use a bfs search similar to num islands
       except we have a counter for the area
       '''
       if not grid:
           return 0
       rows, cols = len(grid), len(grid[0])
       visit = set()
       maxArea = [0]
       def bfs(r,c):
           q = collections.deque()
           visit.add((r,c))
           q.append((r,c))
           currArea = 1
           while q:
               row, col = q.popleft()
               directions = [[1,0],[-1,0],[0,1],[0,-1]]   
               for dr, dc in directions:
                   r,c = row + dr, col + dc
                   if ((r) in range(rows) and
                   (c) in range(cols) and
                   grid[r][c] == 1 and
                   (r, c) not in visit):
                       q.append((r,c))
                       visit.add((r,c))
                       currArea += 1
           if currArea > maxArea[0]:
               maxArea[0] = currArea
       for r in range(rows):
           for c in range(cols):
               if grid[r][c] == 1 and (r,c) not in visit:
                   bfs(r,c)  
       return maxArea[0]
