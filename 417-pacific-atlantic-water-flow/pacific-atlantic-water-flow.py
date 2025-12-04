class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return[]
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        pacific = [[False]*cols for _ in range(rows)]
        atlantic = [[False]*cols for _ in range(rows)]

        q = deque()

        def dfs(row, col, visited):
            visited[row][col] = True
            for (dr, dc) in directions:
                new_row = row + dr
                new_col = col + dc
            
                if new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols:
                    continue
                if visited[new_row][new_col] == True:
                    continue
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                dfs(new_row, new_col, visited)

        # pacific = []
        # atlantic = []
        result = []
        
        for c in range(cols):
            dfs(0, c, pacific)          # top edge
            dfs(rows - 1, c, atlantic)  # bottom edge

        for r in range(rows):
            dfs(r, 0, pacific)          # left edge
            dfs(r, cols - 1, atlantic)

        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])

        return result