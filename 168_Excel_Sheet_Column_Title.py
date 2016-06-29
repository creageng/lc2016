# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = ''
        while n > 26:
            part = n % 26
            n  = n / 26

            if part == 0:
                res = res + "Z"
                n -= 1

            else:
                res  = chr(part + 64) + res

        return chr(n + 64) + res
