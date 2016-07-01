# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0, 0
        res = len(nums) + 1
        currSum = 0

        while r < len(nums):
            currSum += nums[r]
            
            while currSum >= s:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1

            r += 1

        return res if res != len(nums) +1 else 0




class Solution(object):
    def minSubArrayLen(self, s, nums):
        total = left = 0
        res = len(nums) + 1
        for r, n in enumerate(nums):
            total += n
            while total >= s:
                res = min(res, r-l+1)
                l += 1

        return res if res <= len(nums) else 0





class Solution:

    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left



    


