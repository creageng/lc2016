# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# For example, given the range [5, 7], you should return 4.

# [m, n]范围的按位与的结果为m与n的公共“左边首部（left header）”



class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = 0
        while m != n:
            m >>= 1
            n >>= 1
            p += 1

        return m << p
         