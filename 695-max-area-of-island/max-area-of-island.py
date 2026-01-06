class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        max_area = 0
        # area = 0
        visited = [[False] * cols for _ in range(rows)]
        def dfs(r,c):
            if r< 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            if visited[r][c]:
                return 0
            visited[r][c] = True # Make it visited
            area = 1
            for (dr, dc) in directions:
                nr = dr + r
                nc = dc + c
                area += dfs(nr, nc)
            return area
            
        
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    max_area = max(max_area, dfs(row, col))
        return max_area
        #------------------------
        #------------------------
        # rows = len(grid)
        # cols = len(grid[0])
        # directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # visited = set()
        # max_area = 0

        # def dfs(row, col):
        #     if row < 0 or col < 0 or row >= rows or col >= cols:
        #         return 0
        #     if (row,col) in visited:
        #         return 0 
        #     if grid[row][col] == 0:
        #         return 0
        #     visited.add((row, col))
        #     area = 1
        #     for dr,dc in directions:
        #         nr = row + dr
        #         nc = col + dc
        #         area += dfs(nr, nc)
        #     return area
            
        # area = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         if (row, col) not in visited and grid[row][col] == 1:
        #             # area += dfs(row, col)
        #             max_area = max(max_area, dfs(row,col))
        # return max_area
