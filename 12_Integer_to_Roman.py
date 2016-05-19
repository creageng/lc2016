# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

# Subscribe to see which companies asked this question



class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 
                    'L', 'XL', 'X','IX', 'V','IV','I']

        l = ''
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                l += numerals[i]
        return l






