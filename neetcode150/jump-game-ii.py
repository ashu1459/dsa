class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Solution-1: DP Approach O(n^2)
        # dp = {N-1: [True, 0]}

        # for i in range(N-2, -1, -1):
        #     ans = N
        #     for j in range(i + nums[i], i, -1):
        #         if j >= N or not dp[j][0]:
        #             continue
        #         ans = min(ans, 1 + dp[j][1])
        #     dp[i] = [True, ans]

        # return dp[0][1]

        # Solution-2: Greedy - TC O(n) - https://www.youtube.com/watch?v=9kyHYVxL4fw
        lastIndex, coverage = 0, 0
        ans = 0

        if N == 1:
            return ans

        for i in range(N):
            coverage = max(coverage, i + nums[i])

            if i == lastIndex:
                ans += 1
                lastIndex = coverage

                if lastIndex == N-1:
                    break

        return ans
                