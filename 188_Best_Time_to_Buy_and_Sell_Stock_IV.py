# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.





class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        if k > n/2:
            return self.quickSolve(n, prices)

        dp = [None] * (2 * k + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(min(2 * k, i + 1), 0, -1):
                dp[j] = max(dp[j], dp[j -1] + prices[i] * [1, -1][j % 2])

        return max(dp)

    def quickSolve(self, n, prices):
        s = 0

        for i in range(n - 1):
            if prices[i+1] > prices[i]:
                s += prices[i+1] - prices[i]
        return s







