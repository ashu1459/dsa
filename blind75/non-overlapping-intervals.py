class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        # One solution - TC O(n)
        # ans = 0
        # j, i = 0, 1
        # while i < len(intervals):
        #     if intervals[i][0] < intervals[j][1]:
        #         ans += 1
        #         if intervals[i][1] < intervals[j][1]:
        #             j = i
        #     else:
        #         j = i

        #     i += 1
           
        # return ans

        # another solution - TC O(n)
        ans = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # overlapping
            if start < prevEnd:
                ans += 1
                # we want to remove the bigger end value as it overlaps farthest
                prevEnd = min(prevEnd, end)
            else: # non-overlapping
                prevEnd = end

        return ans