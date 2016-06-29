# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.




class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        # b = ":0{width}b".format(bin(n), width=32)
        # lb = [int(e) for e in b]
        # return sum(lb)
        return bin(n).count('1')


# Think of a number in binary n = XXXXXX1000, 
# n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 
# which is just cancel the last 1

class Solution(object):
    def hammingWeight(self, n):
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c