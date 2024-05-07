class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums = sum(nums)
        total = 0
        
        for n in range(len(nums) + 1):
            total += n
        
        return 0 if sums == total else total - sums
