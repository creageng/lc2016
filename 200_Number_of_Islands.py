# 200. Number of Islands My Submissions QuestionEditorial Solution
# Total Accepted: 50474 Total Submissions: 176603 Difficulty: Medium
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
#  An island is surrounded by water and is 
# formed by connecting adjacent lands horizontally or vertically.
#  You may assume all four edges of the grid are all surrounded by water.



class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        m = len(grid)
        n = len(grid[0])

        islands = 0

        def dfs(i, j, grid):
            grid[i][j] = 'X'

            if i < m - 1 and grid[i+1][j] == "1":
                dfs(i+1, j, grid)

            if j < n - 1 and grid[i][j+1] == "1":
                dfs(i, j+1, grid)

            if j > 0  and grid[i][j-1] == "1":
                dfs(i, j-1, grid)

            if i > 0 and grid[i-1][j] == "1":
                dfs(i-1, j, grid)

        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                if curr == "1":
                    dfs(i, j, grid)
                    islands += 1

        return islands