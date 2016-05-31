# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.





class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        nums = range(1,10)

        # rows
        for r in range(9):
            nums = []
            for c in range(9):
                cell = board[r][c]
                if cell != '.' and cell not in nums:
                    nums.append(cell)
                elif cell in nums:
                    return False

        # cols
        for c in range(9):
            nums = []
            for r in range(9):
                cell = board[r][c]
                if cell != '.' and cell not in nums:
                    nums.append(cell)
                elif cell in nums:
                    return False

        # ### check the middle parts
        # mid = board[3:6, 3:6]
        for r1 in [0, 3, 6]:
            for c1 in [0, 3, 6]:
                nums = []
                for r_off in [0,1,2]:
                    for c_off in [0,1,2]:
                        cell = board[r1+r_off][c1+c_off]
                        if cell != "." and cell not in nums:
                            nums.append(cell)
                        elif cell in nums:
                            return False

        return True












