class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        # workable but TLE
        # ans = []
        # for q in sorted(queries):
        #     minRes = float("inf")
        #     for start, end in intervals:
        #         if start > q:
        #             break
        #         if start <= q <= end:
        #             minRes = min(minRes, end - start + 1)
        #     ans.append(-1 if minRes == float("inf") else minRes)
        # return ans

        # Solution-2: TC: O(nlogn) + O(qlogq)
        minHeap = []
        res, i = {}, 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, [r - l + 1, r])
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = (minHeap[0][0] if minHeap else -1)
        
        return [res[q] for q in queries]
