# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        l = 0
        r = len(nums) - 1
       
        res = [-1,-1]

        while l <= r:
            m = (l+r)/2

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                res[0] = m
                res[1] = m

                i = m - 1
                while i >=0  and nums[i] == target:
                    res[0] = i
                    i -= 1

                i = m + 1
                while i < len(nums) and nums[i] == target:
                    res[1] = i
                    i += 1

                break
        return res













