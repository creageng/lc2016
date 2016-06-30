



class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # nums = sorted(str(n))
        # d = collections.defaultdic(int)
        mem = set()
        while n != 1:
            n  = sum([int(i) ** 2 for i in str(n)])

            if n in mem:
                return False
            else:
                mem.add(n)

        return True




class Solution(object):
    def isHappy(self, n):
        mem = set()

        while n != 1 and n not in mem:
            mem.add(n)
            n = sum([int(i) ** 2 for i in str(n)])

        return n == 1
