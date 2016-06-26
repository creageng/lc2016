# Given an array of integers, every element appears twice except for one. Find that single one.



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for i in range(0, len(nums), 2):
            if i < len(nums) - 2 and nums[i] != nums[i+1]:
                return nums[i]
            elif i == len(nums) - 1:
                return nums[-1]


class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

