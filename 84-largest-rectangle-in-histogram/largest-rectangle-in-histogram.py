class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for ind, height in enumerate(heights):
            cur = ind
            while stack and stack[-1][1] > height:
                
                stack_ind, stack_height = stack.pop()
                max_area = max(max_area, (ind - stack_ind) * stack_height)
                cur  = stack_ind

            stack.append((cur, height))   

        for ind, height in stack:
            max_area = max(max_area, height*(len(heights) - ind))
        return max_area
                 

