# Note: This is an extension of House Robber.

# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Credits:


class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n < 4: 
            return max(nums)

        first, second = 0, 0
        for i in nums[:-1]:
            first, second = second, max(first + i, second)

        result = second

        first, second = 0, 0
        for i in nums[1:]:
            first, second = second, max(first + i, second)

        return max(result, second)
        
class Solution2(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        return max(self.robLine(nums[1:]), self.robLine(nums[:-1]))


    def robLine(self, nums):
        n = len(nums)
        odd, even = 0, 0
        for i in range(n):
            if i % 2:
                odd = max(odd+nums[i], even)

            else:
                even = max(even+nums[i], odd)

        return max(odd, even)


class Solution3(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _rob(nums):
            curr = prev = 0
            for num in nums:
                curr, prev = max(curr, prev + num), curr
            return curr

        return max(_rob(nums[len(nums) != 1:]), _rob(nums[:-1])) 




class Solution4(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0], dp[1] = 0, nums[1]

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i - 1])

        res = dp[n-1]

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i-1])

        return max(dp[n-2], res)













