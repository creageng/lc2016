# Given a binary tree, return the zigzag level order traversal of its 
# nodes' values. (ie, from left to right, 
# then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its zigzag level order traversal as:

# [
#   [3],
#   [20,9],
#   [15,7]
# ]



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        res = []
        currlevel = []
        stack = [root]
        l2r = 1

        while stack:
            # access each level as queue
            for i in range(len(stack)):
                node = stack.pop(0)
                currlevel += [node.val]

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            res += [currlevel[::l2r]]
            currlevel = []
            l2r *= -1

        return res











        











