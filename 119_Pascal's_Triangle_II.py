

# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

# Subscribe to see which companies asked this question




class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex <= 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        res = []
        res.append(1)

        preList = self.getRow(rowIndex - 1)
        for i in range(len(preList) - 1):
            res.append(preList[i] + preList[i + 1])

        res.append(1)
        return res