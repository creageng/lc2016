#  Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively. 



class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        end_zero = 0
        start_two = len(nums)
        curr = 0

        while curr < start_two:
            if nums[curr] == 0:
                nums[end_zero], nums[curr] = nums[curr], nums[end_zero]
                end_zero += 1
                curr += 1

            elif nums[curr] == 1:
                curr += 1

            else:
                start_two -= 1
                nums[curr], nums[start_two] = nums[start_two], nums[curr]



