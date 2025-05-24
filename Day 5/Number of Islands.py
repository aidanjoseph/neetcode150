class Solution:
   def numIslands(self, grid: List[List[str]]) -> int:
       #Thoughts
       '''
       Used a linked list or a list to store 1's
       Hashmpa if connected
       bfs
       '''
       if not grid:
           return 0
       rows, cols = len(grid), len(grid[0])
       visit = set()
       islands = 0
       def bfs(r,c):
           q = collections.deque()
           visit.add((r,c))
           q.append((r,c))
           while q:
               row, col = q.popleft()
               directions = [[1,0],[-1,0],[0,1],[0,-1]]    
               for dr, dc in directions:
                   r,c = row + dr, col + dc
                   if ((r) in range(rows) and
                   (c) in range(cols) and
                   grid[r][c] == "1" and
                   (r, c) not in visit):
                       q.append((r,c))
                       visit.add((r,c)) 
