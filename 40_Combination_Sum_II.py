# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return

        if target == 0:
            res.append(path)
            return

        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
             # avoid repeats
            self. dfs(nums,target-nums[i], i+1, path + [nums[i]], res)






class Solution2:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        Solution.res = []
        candidates.sort()
        self.dfs(candidates,0,[],target)
        return Solution.res

    def dfs(self,candidates,start,currlist,target):
        # end = len(candidates)
        if target == 0 and currlist not in Solution.res:
            return Solution.res.append(currlist)    

        for i in range(start,len(candidates)):
            if candidates[i] > target:
                return
            else:
                # self.dfs(candidates,start+1,currlist+[candidates[i]],target-candidates[i])
                self.dfs(candidates,i+1,currlist+[candidates[i]],target-candidates[i])


