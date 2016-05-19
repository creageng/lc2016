# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        res = set()
        
        d  = collections.defaultdict(set)

        for p in xrange(len(nums)):
            for q in xrange(p+1, len(nums)):
                d[nums[p] + nums[q]].add((p,q))

        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                half = target-nums[i]-nums[j]
                if half in d:
                    k_tuple = d[half]
                    for k in k_tuple:
                        if k[0] > j:
                            res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return map(list, res)








        




