# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
# Subscribe to see which companies asked this question


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
          return [nums]

        res = []
        nums.sort()
        prevNum = None

        for i in range(len(nums)):
            if nums[i] == prevNum:
                continue
            
            prevNum = nums[i]
            for permute in self.permuteUnique(nums[:i]+nums[i+1:]):
                res.append([nums[i]]+permute)

        return res

