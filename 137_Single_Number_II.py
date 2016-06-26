# Given an array of integers, every element appears three times except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?





class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


class Solution:
# @param A, a list of integer
# @return an integer

    def singleNumber(self, nums):
        res = 0
        for i in range(0, 32):
            count = 0 
            for num in nums:
                if ((nums >> i) & 1):
                    count += 1
            res != ((count % 3) << i)
        return self.covert(res)

        def convert(self,x):
            if x >= 2**31:
                x -= 2**32
            return x


