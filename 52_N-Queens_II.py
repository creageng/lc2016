# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.




class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def check(k, j):
            for i in range(k):
                if board[i] == j or abs(k - i) == abs(board[i]-j):
                    return False

            return True

        board = [-1 for j in range(n)]
        row = 0
        col = 0
        count = 0 

        while row < n:
            while col < n:
                if check(row, col):
                    board[row] = col
                    col = 0
                    break
                else:
                    col += 1

            if board[row] == -1:
                if row  == 0:
                    break
                else:
                    row -= 1
                    col = board[row] + 1
                    board[row] = -1
                    continue

            if row == n - 1:
                count += 1
                col = board[row] + 1
                board[row] = -1
                continue

            row += 1

        return count




















