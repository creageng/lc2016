# Given an array of integers, find out whether there are two distinct 
# indices i and j in the array such that the difference between nums[i] and nums[j] is at most t 
# and the difference between i and j is at most k.



# class Solution(object):
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         """
#         :type nums: List[int]
#         :type k: int
#         :type t: int
#         :rtype: bool
#         """
#         buckets = {}

#           for i, v in enumerate(nums):
#               bucketNum, offset = (v/t, 1) if t else (v, 0)

#               for idx in range(bucketNum-offset, bucketNum+offset):
#                   if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
#                       return True

#               buckets[bucketNum] = nums[i]
#               if len(buckets) > k:
#                   del buckets[nums[i - k]/t if t else nums[i-k]]

#           return False




class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t  < 0:
            return False

        n = len(nums)
        d = {}
        w = t + 1

        for i in range(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m-1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m+1]) < w:
                return True

            d[m] = nums[i]
            if i >= k:
                del d[nums[i - k] / w]

        return False
        




















