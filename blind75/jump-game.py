class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)

        # Solution-1: Backtracking is slow: TLE
        # def dfs(i):
        #     if i == N-1:
        #         return True

        #     upperBound = i + nums[i] if i + nums[i] < N else N-1
        #     for j in range(upperBound, i, -1):
        #         if dfs(j):
        #             return True

        #     return False

        # return dfs(0)

        # Solution-2: Using Bottoms-Up Approach(From reverse)
        # prev = 0
        # for i in range(N-2, -1, -1):
        #     prev -= 1
        #     if prev + nums[i] >= 0:
        #         prev = 0
        
        # return not prev 

        # Solution-2: Using Bottoms-Up Approach(From reverse)
        goal = N - 1
        for i in range(N-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return not goal