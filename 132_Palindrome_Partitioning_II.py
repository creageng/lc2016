# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Subscribe to see which companies asked this question



class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0 for i in range(len(s)+1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        
        #the worst case is cutting by each char
        for i in range(len(s) + 1):
            count[i] = len(s) - 1 - i
        # the last one, f[n]=-1

        # for i in range(len(s) - 1, -1, -1):
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and ((j-i) < 2 or p[i+1][j-1]):
                    p[i][j] = True
                    count[i] = min(1+count[j+1],count[i])

        return count[0]