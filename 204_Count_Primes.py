# Description:

# Count the number of prime numbers less than a non-negative number, n.


# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        isPrime = [True] * (n+1)
        isPrime[0], isPrime[1] = False, False
     
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i] ==  True:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False

        return sum(isPrime[:-1])
