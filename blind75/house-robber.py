class Solution:
    def rob(self, nums: List[int]) -> int:
        # Solution-1: Using Input Array: DP
        # nums.append(0)

        # for i in range(2, len(nums)):
        #     nums[i] = nums[i] + (max(nums[i - 2], nums[i - 3]))
        
        # return max(nums[-1], nums[-2])

        # Solution-2: Using vars: DP: https://www.youtube.com/watch?v=73r3KWiEvyk
        nonAdjHouse, adjHouse = 0, 0

        for cur in nums:
            nonAdjHouse, adjHouse = adjHouse, max(cur + nonAdjHouse, adjHouse)
        
        return H2