class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n =len(matrix)
        def isValid(x):
            
            r = n-1
            c = 0
            count = 0
            while r >= 0 and c < n:
                if matrix[r][c] <= x:
                    count += r+1
                    c += 1
                else:
                    r -=1
            return count
                
        # rows = len(matrix)
        # cols = len(matrix[0])
        low = matrix[0][0]
        high = matrix[n-1][n-1]

        while low < high :
            mid = low + (high - low) // 2
            if isValid(mid)>= k:
                high = mid
            else:
                low = mid + 1
        return low

        