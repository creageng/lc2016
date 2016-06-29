
# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 


class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        res = 0
        if len(s) == 0:
            return 0
        while len(s)>1:
            increase = ord(s[0])-64
            s = s[1:]
            res = (res+increase)*26
        res = res+ (ord(s[0])-64)
        return res

class Solution:
     def titleToNumber(self, s):
        return reduce(lambda x, y: x*26 + y, map(lambda x: ord(x) - ord("A") + 1, s))




            