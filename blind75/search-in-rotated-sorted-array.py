class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums, target = [3,1], 3
        # l, r = 0, len(nums) - 1

        # while l < r:
        #     mid = (l + r) // 2

        #     if nums[mid] > nums[r]:
        #         l = mid + 1
        #     else:
        #         r = mid
        
        # minimum = l

        # if nums[minimum] == target:
        #     return minimum

        # if minimum == 0:
        #     nl, nr = 0, len(nums) - 1
        # elif nums[minimum] <= target <= nums[-1]:
        #     nl, nr = minimum, len(nums) - 1
        # elif nums[0] <= target <= nums[minimum-1]:
        #     nl, nr = 0, minimum
        # else:
        #     return -1

        # while nl <= nr:
        #     mid = (nl + nr) // 2

        #     if target > nums[mid]:
        #         nl = mid + 1
        #     elif target < nums[mid]:
        #         nr = mid - 1
        #     else:
        #         return mid

        # return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1

