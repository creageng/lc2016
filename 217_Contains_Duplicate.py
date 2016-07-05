# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

class Solution(object):
    def containsDuplicate(self, nums):
        d = collections.defaultdict(list)
        for num in nums:
            if num not in d:
                d[num] = []
            else:
                return True

        return False



class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return True

        return False
