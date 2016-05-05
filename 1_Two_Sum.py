# array, hashtable

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}

        for i in range(len(nums)):

            remain = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[remain] = i



if __name__ == '__main__':
    print Solution().twoSum([2,7,11,15],9)








