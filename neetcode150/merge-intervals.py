class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # TC - nLogn due to sorting
        intervals.sort()
        
        # newInterval = intervals[0]
        # res = []

        # for i in range(1, len(intervals)):
            
        #     # OVERLAP if there is overlap between last and current interval
        #     if newInterval[0] <= intervals[i][0] <= newInterval[1]:
        #         newInterval = [newInterval[0], max(intervals[i][1], newInterval[1])]
        #     # NO OVERLAP: add last/last-merged interval and set last-interval as newInterval
        #     else:
        #         res.append(newInterval)
        #         newInterval = intervals[i]
        
        # if newInterval:
        #     res.append(newInterval)

        # TC - nLogn due to sorting
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start, end])
        
        return res