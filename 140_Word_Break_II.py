# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].

class Solution(object):
    def check(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True

        return dp[len(s)]

    def wordBreak(self, s, wordDict):
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

    def dfs(self, s, wordDict, sentence):
        if self.check(s, wordDict):
            if len(s) == 0:
                Solution.res.append(sentence[1:])

            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, sentence + " "+ s[:i])


class Solution(object):
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i] + (tail and " " + tail)
                    for j in range(i+1, len(s) + 1)
                    if s[i:j] in wordDict
                    for tail in sentences(j)]
            
            return memo[i]

        return sentences(0)










