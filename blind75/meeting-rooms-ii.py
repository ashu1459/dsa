"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Solution-1: TC:O(n^2)
        # intervals.sort(key = lambda x : x.start)
        # ans = 0
        # prevEnd = intervals[0].end
        # days = []
        # for i in range(1, len(intervals)):
        #     if intervals[i].start < prevEnd:
        #         if days:
        #             slotNotFound = True
        #             for j in range(len(days)):
        #                 if intervals[i].start < days[j].end:
        #                     continue
        #                 else:
        #                     slotNotFound = False
        #                     days[j] = intervals[i]
        #             if slotNotFound:
        #                 days.append(intervals[i])
        #         else:
        #             days.append(intervals[i])
        #     else:
        #         prevEnd = intervals[i].end
        
        # return len(days) + 1

        # Solution-2: TC- O(nlogn)
        # https://youtu.be/FdzJmTCVyJU?si=2ks_pzcmsxa5oNfn&t=425
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])
        res, count = 0, 0
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
                res = max(res, count)
            else:
                e += 1
                count -= 1
        return res

