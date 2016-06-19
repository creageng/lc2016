# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",

# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

# Subscribe to see which companies asked this question


# dynamic programming, string
# # dp[i][j] = m的含义是s1的前i个字母和s2的前j个字母可以成功组成s3的前m个字母

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        dp[0][0] =  True

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s3[i - 1] == s1[i - 1]

        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s3[j-1] == s2[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i-1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                            (dp[i][j-1] and s2[j-1] == s3[i + j -1])

        return dp[len(s1)][len(s2)]


















        