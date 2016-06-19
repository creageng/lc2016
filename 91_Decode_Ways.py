# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

# dynamic programming, string

# #  假设解码函数为h。对于一位数X，只能解码成h[X]。而对于一个两位数XY：
# 1. 如果XY<=26，那么能解码成h[X], h[Y], h[XY]
# 2. 否则，只能解码成h[X], h[Y]
# 由于只要求计算最多的解码方法而并不要求每种解码的结果，所以用DP做更为合适高效。

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [int(s[0] != '0')] if s else [0]

        for i in range(1, len(s)):
            dp.append(dp[i - 1] * (s[i] != '0') + 
            dp[i - 2] * (10 <= int(s[i-1:i+1]) <= 26))

        return dp[-1]




