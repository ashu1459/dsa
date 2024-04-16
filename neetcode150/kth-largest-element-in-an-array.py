class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution-1: TC:O(n+klogn)
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)
        ans = 0

        # TC: running k times
        while k > 0:
            # every pop takes logn TC
            ans = -heapq.heappop(maxHeap)
            k -= 1

        return ans

        # Solution-2 - Use quick select

