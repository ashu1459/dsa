class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # seen = {}
        # nums.sort()
        # res = []
        # # print(nums);exit()
        # for i in range(len(nums) - 2):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     left = i+1
        #     right = len(nums) - 1
        #     target = 0 - nums[i]

        #     while left < right:
        #         if nums[right] < 0:
        #             return res
                
        #         sum_total = nums[left] + nums[right]

        #         if sum_total < target:
        #             left += 1
        #         elif sum_total > target:
        #             right -= 1
        #         else:
        #             res.append([nums[i], nums[left], nums[right]])
        #             left += 1
        #             while left < right and nums[left] == nums[left-1]:
        #                 left += 1
        #                 continue

        #     # seen[nums[i]] = 1

        # return res

        # solution-2 More clearner
        nums.sort()
        res = {}

        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res[tuple([nums[i], nums[left], nums[right]])] = 1
                    left += 1
                    right -= 1

        return res

