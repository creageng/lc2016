



class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        res = ''
        k -= 1
        factorial = 1

        for i in range(1,n):
            factorial *= i

        num = [i for i in range(1, n+1)]
        for i in reversed(range(n)):
            curr = num[k/factorial]
            res += str(curr)
            num.remove(curr)

            if i != 0:
                k %=  factorial
                factorial /= i

        return res


