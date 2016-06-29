# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        r = len(dungeon)
        c = len(dungeon[0])

        # programming to recode health status if the kinght get their
        dp = [[0] * c] *r

        #setup the last health prior to update the cell val status //////
        dp[r-1][c-1] = max(0, -dungeon[-1][-1]) + 1

        # update the val in cell along the way
        for row in range(r-1, -1, -1):
            for col in range(c-1, -1, -1):
                down  = None
                if row + 1 < r:
                    down  = max(1, dp[row+1][col] - dungeon[row][col])

                right = None
                if col + 1 < c:
                    right = max(1, dp[row][col+1]-dungeon[row][col])

                if down and right:
                    dp[row][col] = min(down,right)
                elif down:
                    dp[row][col] = down
                elif right:
                    dp[row][col] = right
        return dp[0][0]




