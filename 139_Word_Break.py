# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

#  Time Limit Exceeded

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """

        n = len(s)

        if s in wordDict:
            return True
        else:
            for i in range(n):
                if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                    return True
            return False


class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True

        return dp[len(s)]












