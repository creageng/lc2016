# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.



class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        d = {num: False for num in nums}
        maxLen = -1
        curr = 0

        for num in d:
            if d[num] is False:
            #label as unvisited
                curr = num + 1
                rightLen = 0
                while curr in d:
                    d[curr] = True
                    curr += 1
                    rightLen += 1

                curr = num - 1
                leftLen = 0
                while curr in d:
                    d[curr] = True
                    curr -= 1
                    leftLen += 1

                maxLen = max(maxLen, rightLen + leftLen + 1)

        return maxLen
