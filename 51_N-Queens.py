# The n-queens puzzle is the problem of placing n
#  queens on an n×n chessboard such that no two queens attack each other.


# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.

# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [-1 for i in range(n)]

        def check(k,j):
            # check if the kth queen can be put in column j
            for i in range(k):
                if board[i] == j or abs(k-i) == abs(board[i] - j):
                    return False
            return True

        def dfs(depth, valuelist):
            if depth == n:
                res.append(valuelist)
                return

            for j in range(n):
                if check(depth, j):
                    board[depth] = j
                    s = '.' * n
                    dfs(depth + 1, valuelist + [s[:j] + 'Q' + s[j + 1:]])

        dfs(0, [])

        return res



