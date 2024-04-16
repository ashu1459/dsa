class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution-1: searching in list is O(n)
        # for i in range(len(nums)-1):
        #     if (target - nums[i]) in nums[i+1:]:
        #         return [i, nums[i+1:].index(target - nums[i]) + i + 1]

        # Solution-2: using hashmap bcoz hashmap has O(1) of searching
        hashMap = {}

        for i, num in enumerate(nums):
            if (target - num) in hashMap:
                return [hashMap[target - num], i]
            hashMap[num] = i
        