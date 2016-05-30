# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

# Subscribe to see which companies asked this question


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        isPositive = True if (dividend > 0 and divisor > 0) or \
            (dividend < 0 and divisor < 0) else False

        dividend = abs(dividend)
        divisor = abs(divisor)

        k = 1

        while dividend > divisor:
            divisor <<= 1
            k <<= 1 ## record the movement

        result = 0

        while dividend > 0 and divisor >= 1:
            if dividend >= divisor:
                dividend -= divisor
                result += k
            divisor >>= 1
            k >>= 1

        if not isPositive:
            result = -result 
            
        return min(max(-2147483648, result), 2147483647)





        