class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        direction = [(0,1), (0,-1), (1,0),(-1,0)]

        fresh = 0
        visited = [[False]*cols for _ in range(rows)]

        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col, 0))
        minutes = 0
        while q:
            r, c, t = q.popleft()   
            minutes = max(minutes, t)

            for (dr,dc) in direction:
                nr = r + dr
                nc = c + dc

                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append((nr, nc, t+1))

        return minutes if fresh == 0 else -1


        






                



