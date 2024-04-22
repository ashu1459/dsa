class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Solution-1
        # if len(nums) == 1:
        #     return [nums[:]]
            
        # for i in range(len(nums)):
        #     first = nums.pop(0)
        #     perms = self.permute(nums)

        #     for perm in perms:
        #         perm.append(first)
            
        #     res.extend(perms)
        #     nums.append(first)          

        # return res

        # Solution-2
        # def backtrack(curr):
        #     if curr >= len(nums):
        #         # make a new list as python lists are mutable and res will store a reference of it and therefore will change the appended list
        #         res.append(nums[:])
        #         return
            
        #     for j in range(curr, len(nums)):
        #         nums[j], nums[curr] = nums[curr], nums[j]
        #         backtrack(curr + 1)
        #         nums[j], nums[curr] = nums[curr], nums[j]
        
        # backtrack(0)
        # return res

        # Solution-3
        def backtrack(reduced_list, paths):
            if not reduced_list:
                res.append(paths)
                return

            for i in range(len(reduced_list)):
                backtrack(reduced_list[:i] + reduced_list[i+1:], paths + [reduced_list[i]])

        backtrack(nums, [])
        return res