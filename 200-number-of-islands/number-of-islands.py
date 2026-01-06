class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = [[False] * cols for _ in range(rows)]
        def dfs(r,c):
            if r< 0 or c < 0 or r >= rows or c >= cols:
                return
            if grid[r][c] == "0":
                return
            if visited[r][c]:
                return
            visited[r][c] = True # Make it visited
            for (dr, dc) in directions:
                nr = dr + r
                nc = dc + c
                dfs(nr, nc)
            
        
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    dfs(row, col)
                    islands += 1
        return islands

