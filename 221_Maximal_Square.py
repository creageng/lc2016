



class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        maxArea = 0

        dp = [[0 for j in range(n)] for i in range(m)]

        dp[0][0] = 1 if int(matrix[0][0]) == 1 else 0

        for i in range(1, m):
            dp[i][0] = 1 if int(matrix[i][0]) == 1 else 0

        for j in range(1,n):
            dp[0][j] = 1 if int(matrix[0][j]) ==  1 else 0

        for i in range(1,m):
            for j in range(1,n):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                maxArea = max(maxArea, dp[i][j])

        return maxArea * maxArea




class Solution(object):
    def maximalSquare(self, matrix):
        dp, maxArea = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))], 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                maxArea = max(maxArea, dp[i][j])
        return maxArea*maxArea





