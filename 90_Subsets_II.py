# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def dfs(depth, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)

            if depth == len(nums):
                return

            for i in range(start, len(nums)):
                dfs(depth+1, i + 1, valuelist+[nums[i]])

        dfs(0,0,[])
        return res