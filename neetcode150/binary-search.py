class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            # i = (l + r) // 2
            # to prevent overflow in case of l and r large value like 2^31
            i = l + ((r - l) // 2)

            if target == nums[i]:
                return i
            elif target > nums[i]:
                l = i + 1
            else:
                r = i - 1

        return -1