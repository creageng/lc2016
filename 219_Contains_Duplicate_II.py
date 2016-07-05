# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
#  and the difference between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i

            else:
                if i - d[nums[i]] <= k:
                    return True

                d[nums[i]] = i

        return False

