class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci series, DP
        cur = 1
        dp = [1, 1]

        for i in range(n - 1):
            cur = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], cur

        return cur