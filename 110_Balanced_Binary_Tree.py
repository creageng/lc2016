# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1. 


# tree, depth-first search



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root)[0]


    def check(self, node):
        
        if node is None:
            return(True, 0)

        LB, Dep_L = self.check(node.left)
        RB, Dep_R = self.check(node.right)
        return (LB and RB and abs(Dep_L - Dep_R) <= 1), max(Dep_R, Dep_L) + 1
