#  Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# array, dynamic programming



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        min_tmp = nums[0]
        max_tmp = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            a = min_tmp * nums[i]
            b = max_tmp * nums[i]
            c = nums[i]
            max_tmp = max(a, b, c)
            min_tmp = min(a, b, c)
            res = max(max_tmp, res)

        return res


        
        