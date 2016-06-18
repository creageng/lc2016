#  Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, 
# with the first five elements of nums being 1, 1, 2, 2 and 3.

# It doesn't matter what you leave beyond the new length. 




class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        slow  = 0
        cnt = 1

        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast - 1]:
                cnt += 1
                if cnt <= 2:
                    slow += 1
                    nums[slow] = nums[fast]
            else:
                cnt = 1
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1






      