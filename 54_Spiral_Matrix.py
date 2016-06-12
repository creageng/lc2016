# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        left = 0
        right  = len(matrix[0]) - 1

        up = 0
        bottom = len(matrix) - 1

        res = []

        while left <= right and up <= bottom:
            if left == right:
                for i in range(up, bottom + 1):
                    res.append(matrix[i][left])
                break

            if up == bottom:
                for j in range(left, right + 1):
                    res.append(matrix[up][j])
                break

            for i in range(left, right + 1):
                res.append(matrix[up][i])

            for j in range(up+1, bottom+1):
                res.append(matrix[j][right])

            for i in reversed(range(left,right)):
                res.append(matrix[bottom][i])

            for i in reversed(range(up + 1, bottom)):
                res.append(matrix[i][left])

            up += 1
            right -= 1
            bottom -= 1
            left += 1

        return res









