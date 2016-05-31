# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# binary search, array



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)/2

            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[l]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid +  1

            elif nums[mid] <= nums[r]:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 




