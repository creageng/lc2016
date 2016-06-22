# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).



class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        nlevels = len(triangle)

        dp = [[0 for j in range(1, level+1)] for level in range(1, nlevels+1)]
        dp[0][0] = triangle[0][0]

        if len(triangle) == 1:
            return dp[0][0]

        for level in range(1, nlevels):

            dp[level][0] = triangle[level][0] +  dp[level-1][0]
            dp[level][level] = dp[level-1][level-1] +  triangle[level][level]

            for index in range(1, level):
                dp[level][index] = min(dp[level-1][index-1], dp[level-1][index]) + \
                    triangle[level][index]

        return min(dp[nlevels - 1])


