class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        # This dp will hold the probabilities of all the possible locations after each step
        dp = [[[0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        
        dp[row][column][0] = 1  # Start at the initial position with probability 1
        
        for steps in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for move in moves:
                        prev_r, prev_c = r + move[0], c + move[1]  # Move back to the previous possible position
                        if 0 <= prev_r < n and 0 <= prev_c < n:  # Ensure the move is on the board
                            dp[r][c][steps] += dp[prev_r][prev_c][steps - 1] / 8.0  # Update probability
        
        total_probability = 0
        for r in range(n):
            for c in range(n):
                total_probability += dp[r][c][k]  # Sum probabilities for all valid positions after k steps
        
        return total_probability

# Example usage:
solution = Solution()
n = 3
k = 2
row = 0
column = 0
print(solution.knightProbability(n, k, row, column))  # Output: Probability value
