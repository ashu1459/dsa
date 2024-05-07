class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = 0
        N = len(cost)
        dp = [-1] * N

        # Solution-1: Recursive O(n) because of DP
        # def dfs(i):
        #     if i >= N:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]

        #     dp1 = dfs(i + 1)
        #     dp2 = dfs(i + 2)
        #     dp[i] = cost[i] + min(dp1, dp2)

        #     return dp[i]
        
        # return min(dfs(0), dfs(1))

        # Solution-2: O(n)
        for i in range(2, N):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[N-1], cost[N-2])
