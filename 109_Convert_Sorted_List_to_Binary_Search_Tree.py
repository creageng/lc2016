# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # length = 0
        # curr = head
        # while curr:
        #   length += 1
        #   curr = curr.next
        # 
        if not head:
            return None

        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.sortedArrayToBST(array)

    def sortedArrayToBST(self, nums):

        if not nums:
            return None

        mid = len(nums)/2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root














