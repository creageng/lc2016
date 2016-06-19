# The gray code is a binary numeral system where two successive values differ in only one bit.

# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

# backtracking
# http://www.jiuzhang.com/solutions/gray-code/


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n == 0:
            return [0]

        left = self.grayCode(n-1)
        reverse_left = left[::-1]

        added = 1 << n - 1
        right = [(each+added) for each in reverse_left]

        return left + right


