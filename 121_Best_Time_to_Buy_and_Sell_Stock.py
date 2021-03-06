# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0

# In this case, no transaction is done, i.e. max profit = 0.



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxProfit, min_price = 0, float("inf")

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            maxProfit = max(maxProfit, profit)

        return maxProfit
        


class Solution2(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0

        dp = [0 for i in range(len(prices))]

        min_price = prices[0]
        dp[0] = 0

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i] -min_price)
        return dp[-1]








