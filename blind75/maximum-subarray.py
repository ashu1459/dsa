class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ans = prev = nums[0]

        # for i in range(1, len(nums)):
        #     prev = max(prev + nums[i], nums[i])
        #     ans = max(ans, prev)
        
        ans = nums[0]
        cur = 0

        for i in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            ans = max(ans, cur)

        return ans