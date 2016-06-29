# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

# If the fractional part is repeating, enclose the repeating part in parentheses.

# For example,

# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".




class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        res = ''
        if numerator/denominator < 0:
            res += '-'

        num = abs(numerator)
        den = abs(denominator)

        if num % den == 0:
            res += str(num / den)
            return res

        res += str(num/den)
        res += '.'

        num %= den
        i = len(res)
        d = {}

        while num:
            if num not in d:
                d[num] = i
            else:
                i = d[num]
                res = res[:i] + "(" + res[i:] + ")"
                return res

            num *= 10
            res += str(num / den)
            num %= den
            i += 1

        return res














