# Follow up for problem "Populating Next Right Pointers in Each Node".

# What if the given tree could be any binary tree? Would your previous solution still work?

# Note:

# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL



# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        curr = root

        while curr:
            prev = None
            firstnode = None
            # flag the first left node at next level
            while curr:
                if firstnode == None:
                    firstnode = curr.left is curr.left else curr.right

                if curr.left:
                    if prev:
                        prev.next = curr.left
                    prev = curr.left

                if curr.right:
                    if prev:
                        prev.next = curr.right
                    prev = curr.right

                curr = curr.next

            curr = firstnode











