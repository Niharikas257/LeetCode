class Solution:
    def numDecodings(self, s: str) -> int:
        # if not s or s[0] == '0':
        #     return 0
        # n = len(s)
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n+1):
        #     one_digit = int(s[i-1])
        #     two_digits = int(s[i-2:i])

        #     if 1<= one_digit<=9:
        #         dp[i] += dp[i-1]
        #     if 10<=two_digits<=26:
        #         dp[i] += dp[i-2]

        # return dp[n]
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == '0':  # If starts with '0', invalid decoding
                return 0
            two_digits = 0
            one_digit = dfs(i+1)
            if i+1 < len(s) and 10<= int(s[i:i+2])<=26:
                two_digits += dfs(i+2)
            result = one_digit + two_digits
            memo[i] = result
            return result
        return dfs(0)