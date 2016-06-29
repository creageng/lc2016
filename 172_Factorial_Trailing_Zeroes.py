# Given an integer n, return the number of trailing zeroes in n!.

# Note: Your solution should be in logarithmic time complexity.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question

# Show Tags
# Show Similar Problems



class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        den = 5
        cnt = 0

        while den <= n:
            cnt += n/den
            den *= 5

        return cnt