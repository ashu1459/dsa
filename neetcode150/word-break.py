class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[N] = True

        for i in range(N - 1, -1, -1):
            for w in wordDict:
                wl = len(w)
                if i + wl <= N and s[i: i + wl] == w:
                    dp[i] = dp[i + wl]
                if dp[i]:
                    break
        
        return dp[0]