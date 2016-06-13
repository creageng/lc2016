# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18]. 



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if intervals == []:
            return []

        #sort intervals by starting value
        startings = [interval.start for interval in intervals]
        index = sorted(range(len(startings)), key = lambda k: startings[k])
        sintervals = [intervals[i] for i in index]


        # check the latter interval in previous interval
        res = [sintervals[0]]

        for s in sintervals[1:]:
            # if start large than end of previous interval
            if s.start > res[-1].end:
                res.append(s)
            elif s.start == res[-1].end:
                res[-1].end = s.end
            else:
                ## end of the interval evaluate with the last elment 
                # of the intervasl
                if s.end <= res[-1].end:
                    pass
                else:
                    res[-1].end = s.end

        return res


