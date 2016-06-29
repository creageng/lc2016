# Given an array of size n, find the majority element. 

# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        d = {}

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1


        for (k,v) in d.items():
            if v > len(nums) / 2:
                return k


class Solution(object):
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)/2]