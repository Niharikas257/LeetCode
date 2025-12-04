class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False]*cols for _ in range(rows)]

        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>= cols:
                return 
            if visited[r][c]:
                return
            if grid[r][c] == "0":
                return
            visited[r][c] = True
            for dr, dc in direction:
                dfs(r+dr, c+dc)

        islands = 0

        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == "1":
                    islands += 1
                    dfs(row,col)

        return islands
            


        