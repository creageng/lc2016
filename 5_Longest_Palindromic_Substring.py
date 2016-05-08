

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

       	dp  = [[0 for  i in range(len(s))] for j in range(len(s))]

       	maxL  = 0
       	res = ''

        ##=========================
        #base function
       	for i in range(len(s)):
       		dp[i][i] = 1

        ##=========================
        # transition


        for j in range(len(s)):
       		for i in range(j-1):
       			if s[i] == s[j]:
       				dp[i][j] = dp[i+1][j-1] or ((j-i) <= 2) 
       			
       			if dp[i][j]:
       				if (j-i+1 > maxL):
	       				maxL = j-i+1
	       				res = s[i: j+1]
       	return res

       	# for i in range(len(s)-1):
       	# 	for j in range(i):
       	# 		if s[i-1] == s[j+1]:
       	# 			dp[i][j] = dp[i-1][j+1] + 2

       	# 		if dp[i][j] > maxL:
       	# 			maxL = dp[j][j]
       	# 			res = s[i-1: j+1]
       	# return res









