# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# tree, breath-first search

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        # in the first stage, we store the nodes, not the values
        res = []
        nextLayer = [root]

        while len(nextLayer) != 0:
            res.append(nextLayer)

            # gather the nodes in the next depper layer
            nextLayer = []
            for father in res[-1]:
                if father.left:
                    nextLayer.append(father.left)
                if father .right:
                    nextLayer.append(father.right)

        res = [[node.val for node in layer] for layer in res[::-1]]
        return res
        