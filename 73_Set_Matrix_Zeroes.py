
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# click to show follow up.

# Subscribe to see which companies asked this question


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        

        ## use first row and col as flagged space
        if matrix == 0 or len(matrix) == 0:
            return 


        row1_zero = False
        col1_zero = False

        if 0 in matrix[0]:
            row1_zero = True

        if len([matrix[i][0] for i in range(len(matrix)) if matrix[i][0] == 0]) > 0:
            col1_zero = True

        # scan to locate 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # base on the all the flag in first row and col set 0 to 
     #the cell 
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # reverse back row1 and col1 zero:
        if row1_zero:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if col1_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
