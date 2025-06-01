class Solution:
   def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       #thoughts
       '''
       i mean base cases
       top right and bottom left are always gonna be triviall true i think?
       also if its a 1x1 grid then that is always in it
       how would we do this now?
       if i can reach the top row/left col and the right col and bottom row form a square then its true, seems more like a dfs then a bfs
       do i call it on every square tho?
       seems inefficient
       xt
       #more clever start from pacfici oecan
       see what can reach pacific
       #then do atlatnic, see what can reach atlatnic return that overlap
       '''
       rows, cols = len(heights), len(heights[0])
       pac, atl = set(), set()
       def dfs(r,c,visit, prevHeight):
           if ((r,c) in visit or r < 0 or c < 0 or r == rows or c == cols
           or heights[r][c] < prevHeight):
               return
           visit.add((r,c))
           dfs(r+1, c, visit, heights[r][c])
           dfs(r-1, c, visit, heights[r][c])
           dfs(r, c+1, visit, heights[r][c])
           dfs(r, c-1, visit, heights[r][c])
       for c in range(cols):
           dfs(0, c, pac, heights[0][c])
           dfs(rows - 1, c, atl, heights[rows-1][c])
       for r in range(rows):
           dfs(r, 0, pac, heights[r][0])
           dfs(r, cols -1, atl, heights[r][cols - 1])
       res = []
       for r in range(rows):
           for c in range(cols):
               if (r,c) in pac and (r,c) in atl:
                   res.append([r,c])
       return res
