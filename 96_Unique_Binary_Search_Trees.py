# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# tree, dynamic programming


# 总结规律：
# f(0) = 1
# f(n) = f(0)*f(n-1) + f(1)*f(n-2) + ... + f(n-2)*f(1) + f(n-1)*f(0)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0 for i in range(n+1)]
        nums[0] = 1

        for i in range(1, n+1):
            for j in range(i):
                nums[i] += nums[j] * nums[i - j -1]

        return nums[n]



