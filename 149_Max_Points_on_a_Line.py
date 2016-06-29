# Given n points on a 2D plane, find the maximum 
# number of points that lie on the same straight line.



# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        if len(points) < 3:
            return len(points)

        res = -1
        for i in range(len(points)):
            slope = {'inf':0}
            # hash table to store the slope
            samePointsNum = 0

            for j in range(i+1, len(points)):
                if points[j].x == points[i].x and \
                    points[j].y != points[i].y:
                    slope['inf'] += 1
                elif points[j].x == points[i].x and \
                    points[j].y == points[i].y:
                    samePointsNum += 1
                else:
                    k = 1.0 * (points[j].y - points[i].y)/(points[j].x - points[i].x)
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1

            res = max(res, max(slope.values()) + samePointsNum + 1)

        return res



