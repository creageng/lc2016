#  Given a set of distinct integers, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def dfs(depth, start, vallist):
            res.append(vallist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, vallist+ [nums[i]])
        dfs(0, 0, [])
        return res

# DFS recursively 
class Solution2(object):
    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

# Iteratively
class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [each + [num] for each in res]
        return res










