class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # if not heights or not heights[0]:
        #     return[]
        # rows = len(heights)
        # cols = len(heights[0])
        # directions = [(0,1), (0,-1), (1,0), (-1,0)]
        # pacific = [[False]*cols for _ in range(rows)]
        # atlantic = [[False]*cols for _ in range(rows)]

        # def dfs(row, col, visited):
        #     if row < 0 or col <0 or row>= rows or col >= cols:
        #         return
        #     if visited[row][col]:
        #         return
        #     visited[row][col] = True
        #     for (dr, dc) in directions:
        #         nr = row + dr
        #         nc = col + dc

        #         if nr < 0 or nc <0 or nr>= rows or nc >= cols:
        #             continue
        #         if visited[nr][nc] == True:
        #             continue
        #         if heights[nr][nc] < heights[row][col]:
        #             continue
        #         dfs(nr, nc, visited)
        # result = []
        # for c in range(cols):
        #     dfs(0, c, pacific)
        #     dfs(rows-1, c, atlantic)
        # for r in range(rows):
        #     dfs(r, 0, pacific)
        #     dfs(r, cols-1, atlantic)
        # for row in range(rows):
        #     for col in range(cols):
        #         if pacific[row][col] and atlantic[row][col]:
        #             result.append([row, col])
        #             # print(result)
        # return result

        rows = len(heights)
        cols = len(heights[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        pacific = [[False]* cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(row, col, visited):
            if row < 0 or col < 0 or row >= rows or col>= cols:
                return
            if visited[row][col]:
                return
            visited[row][col] = True
            for (dr, dc) in directions:
                nr = dr + row
                nc = dc + col
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                if visited[nr][nc] :
                    continue
                if heights[nr][nc] < heights[row][col]:
                    continue
                dfs(nr, nc, visited)
        result = []
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows-1, c, atlantic)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols-1, atlantic)
        for row in range(rows):
            for col in range(cols):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])
        return result