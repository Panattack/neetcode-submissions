"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)

        for i in range(1, len(intervals)):
            int2 = intervals[i]
            int1 = intervals[i - 1]

            if int2.start < int1.end:
                return False
        
        return True