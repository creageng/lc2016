# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.

# Subscribe to see which companies asked this question


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) / 2

            if target == nums[m]:
                return True

            if nums[l] < nums[m]:
                 # // left half sorted
                 if nums[l] <= target <= nums[m]:
                    r = m - 1
                 else:
                    l = m + 1
            elif nums[l] > nums[m]:
                # // right half sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # skip duplicates
                l += 1
        return False










        


