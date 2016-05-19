# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume 
# that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closeDiff = 10000
        res = 0

        if len(nums) < 3:
            return []

        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = len(nums)-1

            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                diff = abs(sum_3-target)

                if diff < closeDiff:
                    closeDiff = diff
                    res = sum_3

                if sum_3 == target:
                    return sum_3
                elif sum_3 < target:
                    left += 1
                else:
                    right -= 1
        return res




                

