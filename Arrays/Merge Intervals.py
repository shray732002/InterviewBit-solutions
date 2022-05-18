#Problem
"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
 def insert(self,intervals, new_interval):
    if(new_interval.start>new_interval.end):
        temp=new_interval.start
        new_interval.start=new_interval.end 
        new_interval.end=temp
    if(len(intervals)==0):
        intervals.append(Interval(new_interval.start,new_interval.end))
        return intervals
    for i in range(len(intervals)):
        if(new_interval.start>=intervals[i].start and new_interval.start<=intervals[i].end):
            begn=intervals[i].start
            break
        else:
            begn=new_interval.start
    for i in range(len(intervals)):
        if (new_interval.end>=intervals[i].start and new_interval.end<=intervals[i].end):
            endn = intervals[i].end
            break
        else:
            endn = new_interval.end
    i=0
    n=len(intervals)
    while(n):
        if(i==len(intervals)):
            break 
        if(intervals[i].start<begn):
            i+=1
        if(i==len(intervals)):
            break    
        if((intervals[i].start>=begn and intervals[i].end<=endn)):
            intervals.pop(i)
        n-=1
    intervals.insert(i,Interval(begn,endn))
    return intervals
