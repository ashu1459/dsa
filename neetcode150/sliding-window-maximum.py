class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <= k:
            return [max(nums)]
        
        # Brute-force
        # l, max_index = 0, 0
        # res = []

        # for r in range(k-1, len(nums)):
        #     res.append(max(nums[l:r+1]))
        #     l+=1
        
        # return res

        # solution-2: O(n)
        l, r = 0, 0
        q = collections.deque()
        res = []

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res
