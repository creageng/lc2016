# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?


#greedy

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        #every kids must at least have one candy
        candies = [1] * n

        for i in range(n - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1

        for i in range(n-1, 0, -1):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1

        return sum(candies)





