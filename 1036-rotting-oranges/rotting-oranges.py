# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         direction = [(0,1), (0,-1), (1,0),(-1,0)]

#         fresh = 0
#         visited = [[False]*cols for _ in range(rows)]

#         q = deque()

#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == 1:
#                     fresh += 1
#                 if grid[row][col] == 2:
#                     q.append((row, col, 0))
#         minutes = 0
#         while q:
#             r, c, t = q.popleft()   
#             minutes = max(minutes, t)

#             for (dr,dc) in direction:
#                 nr = r + dr
#                 nc = c + dc

#                 if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
#                     grid[nr][nc] = 2
#                     fresh-=1
#                     q.append((nr, nc, t+1))

#         return minutes if fresh == 0 else -1

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # dist[r][c] = earliest minute this cell becomes rotten
        INF = 10**9
        dist = [[INF] * cols for _ in range(rows)]

        fresh_cells = []

        # Collect all starting rotten oranges
        starts = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    starts.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cells.append((r, c))

        # If no fresh, answer is 0
        if not fresh_cells:
            return 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r: int, c: int, t: int) -> None:
            # Out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # Empty cell blocks spread
            if grid[r][c] == 0:
                return

            # If we already found an equal or faster time to reach this cell, stop
            if t >= dist[r][c]:
                return

            # Record improved earliest time
            dist[r][c] = t

            # Keep spreading
            for dr, dc in directions:
                dfs(r + dr, c + dc, t + 1)

        # Multi-source DFS relaxation: start DFS from every rotten orange at time 0
        for r, c in starts:
            dfs(r, c, 0)

        # Answer is the maximum earliest-time among fresh oranges, if all reachable
        ans = 0
        for r, c in fresh_cells:
            if dist[r][c] == INF:
                return -1
            ans = max(ans, dist[r][c])

        return ans



        






                



