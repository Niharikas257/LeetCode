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

    # def _largestRectangleArea(self, heights):
    def _largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack of (start_index, height)
        # start_index tells how far left this height can extend.
        stack = []
        best = 0

        for i, h in enumerate(heights):
            start = i

            # If current height is smaller, we must close rectangles that are taller than h
            while stack and stack[-1][1] > h:
                prev_start, prev_height = stack.pop()

                # Rectangle of height prev_height spans from prev_start to i - 1
                area = prev_height * (i - prev_start)
                if area > best:
                    best = area

                # Current bar of height h can extend as far left as prev_start
                start = prev_start

            # Push current height with the earliest start it can use
            stack.append((start, h))

        # Close any rectangles that extend to the end of the histogram
        n = len(heights)
        while stack:
            start, h = stack.pop()
            area = h * (n - start)
            if area > best:
                best = area

        return best
        

        