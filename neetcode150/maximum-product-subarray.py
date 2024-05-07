class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Solution-1: TC - O(n)
        # res = max(nums)
        # curMax, curMin = 1, 1

        # for n in nums:
        #     if n == 0:
        #         curMax, curMin = 1, 1
            
        #     temp = curMax
        #     curMax = max(n * curMax, n * curMin, n)
        #     curMin = min(n * temp, n * curMin, n)
        #     res = max(res, curMax)
        
        # return res

        # Solution-2: TC - O(n) - https://www.youtube.com/watch?v=Y6B-7ZctiW8
        N = len(nums)
        ans = nums[0]
        leftRange, rightRange = 1, 1

        for i in range(N):
            leftRange = 1 if leftRange == 0 else leftRange
            rightRange = 1 if rightRange == 0 else rightRange

            leftRange *= nums[i]
            rightRange *= nums[N - 1 - i]

            ans = max(ans, leftRange, rightRange)
        
        return ans

        