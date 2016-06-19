# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# # Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
        	return []

        nextLayer = [root]
        res = []

        while len(nextLayer) != 0:
            res.append(nextLayer)
            
            # gather the nodes in next level
            nextLayer = []
            for father in res[-1]:
                if father.left != None:
                    nextLayer.append(father.left)
                if father.right != None:
                    nextLayer.append(father.right)

        # # in the second stage, we conver the nodes into their values
        res = [[node.val for node in layer] for layer in res]
        return res


















        	
        


