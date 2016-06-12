# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6. 


# array, dynamic programming, divide and conquer


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums[0] > 0:
            currSum = nums[0]
        else:
            currSum = 0

        maxSum = nums[0]

        for num in nums[1:]:
            currSum += num

            if currSum > maxSum:
                maxSum = currSum

            if currSum < 0:
                currSum = 0

        return maxSum





     #    n = len(nums)
        # dp  = [[0 for i in range(n)] for j in range(n)}

        # for i in range(n):
        #   dp[0][i] = nums[i]
        #   dp[i][0] = nums[i]

        # for i in range(1, n):
        #   for j in range(i,n):
        #       dp[i][j-1] +  nums[j-1]



