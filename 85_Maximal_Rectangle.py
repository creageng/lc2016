

# Given a 2D binary matrix filled with 0's and 1's,
#  find the largest rectangle containing all ones and return its area.

# http://www.cnblogs.com/lichen782/p/leetcode_maximal_rectangle.html

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if matrix == []:
            return 0

        heights = [0 for i in range(len(matrix[0]))]
        maxArea = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            maxArea = max(maxArea, self.largestArea(heights))

        return maxArea


    def largestArea(self, heights):
        stack = []
        i = 0
        maxArea = 0
        h = heights + [0]

        while i < len(h):
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i)
                i += 1
            else:
                tmp = stack.pop()
                maxArea = max(maxArea, h[tmp] * (i if not stack else i - stack[-1] - 1))

        return maxArea







