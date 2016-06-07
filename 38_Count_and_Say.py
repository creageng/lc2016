# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            prev = ''
            newS = ''
            num = 0

            for curr in s:
                if prev != "" and prev != curr:
                    newS += str(num) + prev
                    num = 1
                else:
                    num += 1

                prev = curr

            newS += str(num) + prev
            s = newS

        return s
