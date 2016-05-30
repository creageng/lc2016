#  Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        partitionIndex = -1
        
        # 1, from right to left, find the first digit(PartitonNumber)
        # which violates the increase treand
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1] < nums[i]:
                partitionIndex = i-1
                break

        # 2, from right to left, find the first digit which large than 
        # PartitonNumber, call it changeNumber
        if partitionIndex != -1:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[partitionIndex]:
                    nums[i],nums[partitionIndex] = nums[partitionIndex],nums[i]
                    break
        
        # #4, Reverse all the the digit on the right partion index
        nums[partitionIndex+1:] = nums[partitionIndex+1:][::-1]
        return