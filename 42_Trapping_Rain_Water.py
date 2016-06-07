# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# tag: array, stack and two pointers

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height or len(height) < 3:
            return 0

        v = 0

        l = 0
        r = len(height) - 1

        l_max, r_max = height[l], height[r]

        while l < r:
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)

            if l_max <= r_max:
                v += l_max - height[l]
                l += 1
            else:
                v += r_max - height[r]
                r -= 1

        return v



class Solution2(object):
    def trap(self, height):
        l_high = [0 for i in range(len(height))]
        l_max = 0
        res = 0

        #save left most high heights
        for i in range(len(height)):
            if height[i] > l_max:
                l_max = height[i]
            l_high[i] = l_max

        r_max = 0
        for i in reversed(range(len(height))):
            if height[i] > r_max:
                r_max = height[i]

            currWater = min(l_high[i], r_max) - height[i]
            if currWater > 0:
                res += currWater
        return res            





















