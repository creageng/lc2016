
# # array, two pointers

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maxArea = 0

#         left = 0
#         right = len(height) - 1
#         curr_area = 0

#         if len(height) == 0:
#             return 0

#         while left < right:
#             curr_area = min(height[left], height[right]) * (right-left)
            
#             if left+1 < len(height) -1 and height[left+1] > height[left]:
#                 if maxArea < curr_area:
#                     maxArea = curr_area
#             left += 1

#             if right > 0 and height[right-1] > height[right]:
#                 if maxArea < curr_area:
#                     maxArea = curr_area
#             right -= 1

#         return maxArea


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0

        left = 0
        right = len(height) - 1
        curr_area = 0

        if len(height) == 0:
            return 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right-left)

            if curr_area > maxArea:
                maxArea = curr_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            

        return maxArea

