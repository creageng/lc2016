# Implement int sqrt(int x).

# Compute and return the square root of x.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems

# binary search, math



class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0 or x == 1:
            return x

        l = 1
        r = x/2 + 1

        while l <= r:
            mid = (l+r)/2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1

        return r


