
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# For example:
# Given array A = [2,3,1,1,4]

# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        curMax = 0
        # from 0 to i, the max range can reach

        curRch = 0
        # from nums[0] jump ret times, the max range it can reach

        for i in range(len(nums)):
            if i > curRch:
                ret += 1
                curRch = curMax
            curMax = max(curMax, nums[i] + i)

        return ret
