#  The string "PAYPALISHIRING" is written in 
#  a zigzag pattern on a given number of rows 
#  like this: (you may want to display this pattern 
#   in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this 
# conversion given a number of rows:

# string convert(string text, int nRows);

# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s
        
        res = ['' for i in range(numRows)]

        d = 1 
        # direction
        rowix = 0

        for i in range(len(s)):
            if rowix == numRows-1:
                d = -1
            elif rowix == 0:
                d = 1
            res[rowix] += s[i]
            rowix += d

        return ''.join(res) 








