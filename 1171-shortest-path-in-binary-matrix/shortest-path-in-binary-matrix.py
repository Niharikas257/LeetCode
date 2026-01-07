class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        q = deque()
        q.append((0,0,1))
        grid[0][0] = 1

        # visited = [[False]* cols for _ in range(rows)]
        # visited[0][0] = True
        if rows == 1 and cols == 1:
            return 1
        while q:
            r,c,d = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr>=rows or nc>=cols:
                    continue
                
                if grid[nr][nc] != 0:
                    continue
                if nr == rows-1 and nc == cols-1:
                    return d+1
                grid[nr][nc] = 1
                q.append((nr, nc, d+1))
        return -1
        