class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # if x < 0:
        #     return self.reverse(-x) * (-1)

        # return int(str(x)[::-1])

        sign = cmp(x,0)
        r = int(str(x*sign)[::-1])
        return sign * r * (r < 2 ** 31)