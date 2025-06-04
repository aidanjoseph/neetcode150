class Solution:
   def solve(self, board: List[List[str]]) -> None:
       """
       Do not return anything, modify board in-place instead.
       """
       #thoughts
       '''
       idk how u use a bfs or dfs
       but i suppose maybe just call it on an o
       if you can reach any edge of the board then u cant capture it
       if u do then u can capture it, maybe mark with a # or some shit for capture
       #or run dfs on the edge regions so we can find what we don't wanna capture
       make them as something
       '''
       rows, cols = len(board), len(board[0])
       def capture(r,c):
           if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
               return
           board[r][c] = "T"
           capture(r+1,c)
           capture(r-1,c)
           capture(r,c+1)
           capture(r,c-1)
       #1. Capture unsorronded regions (O --> T)
       for r in range(rows):
           for c in range(cols):
               if board[r][c] == "O" and (r in [0, rows -1]
               or c in [0, cols -1]):
                   capture(r,c)
       #2. Capture surronded regions O-->X
       for r in range(rows):
           for c in range(cols):
               if board[r][c] == "O":
                   board[r][c] = "X"
       #3. Uncaputre surronede regions T--> O
       for r in range(rows):
           for c in range(cols):
               if board[r][c] == "T":
                   board[r][c] = "O"
