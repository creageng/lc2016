# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

# Try to solve it in linear time/space.

# Return 0 if the array contains less than 2 elements.

# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return 0

        nums = self.radixsort(nums)
        res = abs(nums[0] - nums[1])
        for i in range(2, len(nums)):
            res = max(res, abs(nums[i] - nums[i - 1]))
        return res

    def radixsort(self, nums):
        RADIX = 10
        maxLength = False

        pos, digit = -1, 1

        while not maxLength:
            maxLength = True
            buckets = [[] for _ in range(RADIX)]

            # split a list between lists
            for num in nums:
                pos = num / digit
                buckets[pos % RADIX].append(num)
                if maxLength and pos > 0:
                    maxLength = False

        # unfold the list               
            a = 0
            for b in range(RADIX):
                bucket = buckets[b]
                for i in bucket:
                    nums[a] = i
                    a += 1

        # move to next digit
            digit *=  RADIX

        return nums





class Solution2(object):
    def maximumGap(self, nums):

        if len(nums) < 2:
            return 0

        minNum = -1
        maxNum = -1
        n = len(nums)

        minNum = min(nums)
        maxNum = max(nums)

        if minNum == maxNum:
            return 0

        avarage = (maxNum - minNum) / (n - 1)

        localMin = [ -1 for i in range(n)]
        localMax = [ -1 for i in range(n)]

        for i in range(n):
            t = (num[i] - minNum)/avarage
            localMin[t] = self.min(localMin[t], nums[i])
            localMax[t] = self.max(localMax[t], nums[i])

        ans = avarage
        l = 0
        r = 1

        while l < n - 1:
            while r < n and localMin[r] == -1:
                r += 1
            if r >= n: break
            ans = self.max(ans, localMin[r] - localMax[l])
            l = r
            r += 1

        return ans

    def min(self, a, b):
        if (a==-1): return b
        elif (b==-1): return a
        elif (a<b): return a
        else: return b

    def max(self, a, b):
        if (a==-1): return b
        elif (b==-1): return a
        elif (a>b): return a
        else: return b    
























