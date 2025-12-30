class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0
            max_area = max(max_area, self._largestRectangleArea(heights))

        return max_area

    def _largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for i, h in enumerate(heights):
            cur = i
            while stack and stack[-1][1] > h:
                prev_start, prev_height = stack.pop()
                area = prev_height * (i - prev_start)
                best = max(best, area)
                cur = prev_start
            stack.append((cur, h))

        # Close any rectangles that extend to the end of the histogram
        n = len(heights)
        while stack:
            start, h = stack.pop()
            area = h * (n - start)
            best = max(best, area)

        return best
        

        