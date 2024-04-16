class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
        if len(nums) == 0:
            return 0
        # solution-1 - O(nlogn) becauase of sorting
        # nums.sort()

        # maximum = 1
        # res = [1]

        # for i in range(len(nums)):
        #     if i == 0 or nums[i-1] == nums[i]:
        #         continue
        #     if nums[i-1] + 1 == nums[i]:
        #         maximum += 1
        #     elif maximum > 1:
        #         res.append(maximum)
        #         maximum = 1

        # res.append(maximum)

        # return max(res)

        # solution-2 O(n)
        hashmap = set(nums)
        res = 1
        
        for num in nums:
            # skip if its not the starting number
            if num - 1 in hashmap:
                continue

            maximum = 1
            while num + maximum in hashmap:
                maximum += 1

            if maximum > 1:
                res = max(maximum, res)
        return res