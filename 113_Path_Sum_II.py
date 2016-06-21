#  Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# For example:
# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1

# return

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, currList, res):
        if not root:
            return

        if root.left is None and root.right is None and root.val == sum:
            res. append(currList + [root.val])

        self.dfs(root.left, sum-root.val, currList + [root.val], res)
        self.dfs(root.right, sum-root.val, currList+[root.val], res)













