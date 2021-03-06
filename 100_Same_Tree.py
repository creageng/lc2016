# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.



# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if p.val != q.val:
        #     return False
        if p is None or q is None:
            if p is None and q is None:
                return True
            else:
                return False
        else:
            if self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right) and \
            p.val == q.val:
                return True
            else:
                return False

