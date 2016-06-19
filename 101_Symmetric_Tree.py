# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# tree, dfs, bfs


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        stack = []
        stack.append((root.left, root.right))

        while stack:
            l,r = stack.pop()

            if not l and not r:
                continue
            elif l and r and l.val == r.val:
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
            else:
                return False

        return True


        