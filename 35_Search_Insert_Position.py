# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0



class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l  = 0
        r = len(nums)
        
        if target > nums[-1]:
        	return len(nums)

        while l <= r:
        	m = (l + r)/2

        	if nums[m] == target:
        		return m

        	if m > 1 and nums[m-1] < target < nums[m]:
        		return m	


        	if nums[m] < target:
        		l = m+1
        	else:
        		r = m-1
        return l


