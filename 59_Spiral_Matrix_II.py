# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]



class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        if n <= 0:
            return []

        matrix = [row[:] for row in [[0]*n] *n]
        row_st = 0
        row_end = n-1

        col_st = 0
        col_end = n-1
        curr = 1

        while True:
            if curr > n*n:
                break

            for c in range(col_st, col_end+1):
                matrix[row_st][c] = curr
                curr += 1

            row_st += 1

            for r in range(row_st, row_end+1):
                matrix[r][col_end] = curr
                curr += 1
            col_end -= 1

            for c in range(col_end, col_st-1, -1):
                matrix[row_end][c] = curr
                curr += 1
            row_end -= 1

            for r in range(row_end, row_st-1, -1):
                matrix[r][col_st] = curr
                curr += 1
            col_st += 1

        return matrix




