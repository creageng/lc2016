# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for j in range(n)] for i in range(m)]

        i, j = 0, 0

        while i < m:
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1
            i += 1

        for _tmp in range(i, m):
            dp[_tmp][0] = 0

        while j < n:
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
                break
            else:
                dp[0][j] = 1
            j += 1

        for _tmp in range(j, n):
            dp[0][_tmp] = 0

        for i in range(1, m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]




        