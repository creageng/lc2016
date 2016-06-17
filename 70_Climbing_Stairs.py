# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Subscribe to see which companies asked this question



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res  = []
        res.append(1)
        res.append(1)

        for i in range(2, n+1):
            res.append(res[i-1] + res[i-2])

        return res[n]

