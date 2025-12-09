class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1 2 3     7 4 1  
        # 4 5 6     8 5 2
        # 7 8 9     9 6 3

        # 1 4 7
        # 2 5 8
        # 3 6 9

        # grid[i][j] = 1 / grid[j][i] 
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            left = 0
            right = n-1
            while left < right:
                matrix[i][right], matrix[i][left] = matrix[i][left], matrix[i][right]
                left += 1
                right -= 1

