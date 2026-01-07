class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        INF = 10**18
        best = [[INF] * cols for _ in range(rows)]
        best[0][0] = 0
        heap = [(0, 0, 0)] # effort, r, c
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            effort, r, c = heapq.heappop(heap)

            # If this heap entry is stale, skip it.
            if effort != best[r][c]:
                continue
            if r == rows - 1 and c == cols - 1:
                return effort
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                # if the new weight < already presnt distance, update the distance step
                edge_diff = abs(heights[r][c] - heights[nr][nc])
                new_effort = max(effort, edge_diff)
                if new_effort < best[nr][nc]:
                    best[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))
        return -1
