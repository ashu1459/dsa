class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2:
            return False

        DP = set()
        DP.add(0)
        target = sums // 2

        for num in nums:
            if num == target:
                return True
            nextDp = set()
            for d in DP:
                if d + num == target:
                    return True
                nextDp.add(d + num)
                nextDp.add(d)
            DP = nextDp
        
        return True if target in DP else False
                