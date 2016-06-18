#  Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]



class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """ 
        a = range(1, n + 1)
        return self.dfs(a, k)

    def dfs(self, a, k):
        if k == 0:
            return [[]]
        elif k == len(a):
            return [a]
        else:
            res = []
            for i, e in enumerate(a):
                res_comb =  self.dfs(a[i+1:], k-1)
                for comb in res_comb:
                    comb.insert(0, e)
                res += res_comb
            return res




class Solution2(object):
    def combine(self, n, k):
        if k == 1:
            return [[i] for i in range(1,n+1)]
        elif k == n:
            return [[i for i in range(1,n+1)]]
        else:
            res = []
            res += self.combine(n-1,k)
            part = self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            res += part
            return res
















