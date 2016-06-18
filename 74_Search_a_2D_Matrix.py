# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]

# Given target = 3, return true.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if matrix is None or len(matrix) == 0:
            return False

        start = 0
        
        m = len(matrix)
        n = len(matrix[0])
        end = m * n - 1

        while start <= end:
            # mid = (l + r)/2
            # mid = (start + end)/2
            mid = start + (end - start)/2
            tmp = matrix[mid/n][mid%n]
            
            if tmp == target:
                return True
            elif tmp < target:
                start = mid + 1
            else:
                end = mid -1

        return False

        










