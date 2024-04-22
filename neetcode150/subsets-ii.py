class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        subsets = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            # decision to include current
            subsets.append(nums[i])
            dfs(i + 1)

            # decision NOT to include current
            subsets.pop()
            # to remove duplicates, keep shifting pointer, eg: [1,2,2,2,3]
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res
        