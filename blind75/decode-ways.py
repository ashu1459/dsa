class Solution:
    def numDecodings(self, s: str) -> int:
        # https://www.youtube.com/watch?v=FEkZxCl_-ik
        N = len(s)
        dp = [1] * N

        if s[0] == '0':
            return 0

        # cur_ways = ways(i-1) if last digit valid + ways(i-2) if last two digits valid
        for i in range(1, N):
            temp = 0
            if 0 < int(s[i]) <= 9:
                temp += dp[i - 1]
            if s[i - 1] != '0' and 0 < int(s[i-1:i+1]) <= 26:
                temp += dp[i - 2] if i > 1 else 1
            
            dp[i] = temp

        return dp[N-1]