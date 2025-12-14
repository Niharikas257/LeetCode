class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # rows = len(grid)
        # cols = len(grid[0])
        # dir = [(1,0), (-1,0), (0,1), (0,-1)]
        # visited = set()
        # max_area = 0
        # def dfs(row, col):
        #     if row < 0 or col < 0 or row == rows or col == cols:
        #         return 0
        #     if (row, col) in visited:
        #         return 0
        #     if grid[row][col] == 0:
        #         return 0
        #     area = 1
        #     visited.add((row, col))
        #     for dr, dc in dir:
        #         area += dfs(row+dr, col+dc)
        #     return area
        # for row in range(rows):
        #     for col in range(cols):
        #         if (row, col) not in visited and grid[row][col] == 1:
        #             dfs_area = dfs(row, col)
        #             max_area = max(max_area, dfs_area)
        # return max_area


        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        max_area = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0
            if (row,col) in visited:
                return 0 
            if grid[row][col] == 0:
                return 0
            visited.add((row, col))
            area = 1
            for dr,dc in directions:
                nr = row + dr
                nc = col + dc
                area += dfs(nr, nc)
            # area = 1  # count this land cell
            # for dr, dc in directions:
            #     area += dfs(r + dr, c + dc)  # add neighbor areas
            # return area
            return area
            
        area = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    # area += dfs(row, col)
                    max_area = max(max_area, dfs(row,col))
        return max_area