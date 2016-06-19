#  Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Example 1:

#     2
#    / \
#   1   3

# Binary tree [2,1,3], return true.

# Example 2:

#     1
#    / \
#   2   3

# Binary tree [1,2,3], return false. 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def ValidBST(self, root, Min, Max):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        if not Min < root.val < Max:
            return False

        return self.ValidBST(root.left, Min, root.val) and \
            self.ValidBST(root.right, root.val, Max)


    def isValidBST(self, root):
        return self.ValidBST(root, float('-inf'), float('inf'))


class Solution(object):
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        self.validate(root)
        return self.isBST

    def validate(self, root):
        if root is None:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        self.lastVal = root.val
        self.validate(root.right)



# python inorder non-recursive solution, using stack

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        curr = root
        prev = None

        while len(stack) or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                p = stack.pop()
                if prev and p.val <= prev.val:
                    return False
                prev = p
                curr = p.right
        return True






