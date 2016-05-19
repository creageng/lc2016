# Write a function to find the longest 
# common prefix string amongst an array of strings.

# Subscribe to see which companies asked this question


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs,key=len)

        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[-1]

        pre = self.longestCommonPrefix(strs[:-1])

        if pre is None:
            return None

        while not strs[-1].startswith(pre):
            pre = pre[:-1]

        return pre








