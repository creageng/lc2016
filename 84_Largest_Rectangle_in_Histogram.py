# Given n non-negative integers representing the histogram's
#  bar height where the width of each bar is 1,
#  find the area of largest rectangle in the histogram.

# array, stack


# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
# 若heightStack为空或者当前高度大于heightStack栈顶，则当前高度和当前下标分别入站。
# 所以heightStack记录了一个连续递增的序列。

# 若当前高度小于heightStack栈顶，heightStack和indexStack出栈，
# 直到当前高度大于等于heightStack栈顶。出栈时，同时计算区间所形成的最大面积。
# 注意计算完之后，当前值入栈的时候，其对应的下标应该为最后一个从indexStack出栈的下标。
# 比如height[2]入栈时，其对应下标入栈应该为1，
# 而不是其本身的下标2。如果将其本身下标2入栈，则计算绿色区域的最大面积时，会忽略掉红色区域。

# http://easyleetcode.blogspot.com/2015/01/leetcode-84-largest-rectangle-in.html


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack  = []
        i = 0
        maxArea = 0
        h = heights + [0]

        while i < len(h):
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i)
                i += 1
                # maintain a stack of non-decreasing height
            else:
                tmp = stack.pop()
                #  do nothring in i
                # pop out the stack element to test the various stack area
                maxArea = max(maxArea, h[tmp] * (i if not stack else i - stack[-1] - 1))
        return maxArea






