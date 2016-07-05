# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


# Example 1:

# Input: k = 3, n = 7

# Output:

# [[1,2,4]]

# Example 2:

# Input: k = 3, n = 9

# Output:

# [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        arr = range(1, 10)
        self.dfs(k, n, [], arr)
        return self.res

    def dfs(self, k, n, pre, post):
        if len(pre) == k and n == 0:
            self.res.append(pre)
        elif n < 0 or len(pre) > k:
            return
        else:
            for i in range(0, len(post)):
                self.dfs(k, n - post[i], pre+[post[i]], post[i+1:])













