class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # rows = len(grid)
        # cols = len(grid[0])
        # dir = [(1,0), (-1,0), (0,1), (0,-1)]
        # visited = [[False]*cols for _ in range(rows)]
        

        # def dfs(row, col):
        #     if row<0 or col<0 or row>= rows or col>= cols:
        #         return
        #     if visited[row][col]:
        #         return
        #     if grid[row][col] == "0":
        #         return
        #     visited[row][col] = True
        #     for dr, dc in dir:
        #         dfs(row+dr, col+dc)
        # islands = 0 
        # for row in range(rows):
        #     for col in range(cols):
        #         if not visited[row][col] and grid[row][col] == "1":
        #             islands += 1
        #             dfs(row, col)
        # return islands


        rows = len(grid)
        cols =len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if (row,col) in visited:
                return
            if grid[row][col] == "0":
                return
            visited.add((row, col))
            for dr,dc in directions:
                nr = row + dr
                nc = col + dc
                dfs(nr, nc)
            return 1
        
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == "1":
                    islands += dfs(row, col)
                    
        return islands




        