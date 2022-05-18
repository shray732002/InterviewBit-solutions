#Problem
"""
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval.start)
        res = []
        first = intervals[0].start
        last = intervals[0].end
        for i in range(1,len(intervals)):
            if last > intervals[i].end:
                continue
            elif last < intervals[i].start:
                res.append(Interval(first,last))
                first = intervals[i].start
                last = intervals[i].end
            else:
                last = intervals[i].end
        res.append(Interval(first,last))
        return res
