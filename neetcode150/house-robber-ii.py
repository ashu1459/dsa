class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N <= 3:
            return max(nums)

        # skip LAST house
        h1, h2 = 0, 0
        for i in range(N - 1):
            h1, h2 = h2, max(nums[i] + h1, h2)

        # skip FIRST house
        h3, h4 = 0, 0
        for j in range(1, N):
            h3, h4 = h4, max(nums[j] + h3, h4)

        return max(h2, h4)
        