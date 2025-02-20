class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':  # Edge case: Cannot start with '0'
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Base cases
        
        for i in range(2, n + 1):
            one_digit = int(s[i-1])   # Last single digit
            two_digits = int(s[i-2:i])  # Last two digits
            
            if 1 <= one_digit <= 9:  # If valid single digit decode
                dp[i] += dp[i-1]
            
            if 10 <= two_digits <= 26:  # If valid double digit decode
                dp[i] += dp[i-2]
        
        return dp[n]
