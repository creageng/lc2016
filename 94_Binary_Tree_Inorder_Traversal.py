# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],

#    1
#     \
#      2
#     /
#    3

# return [1,3,2]. 



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res.extend(self.inorderTraversal(root.left))
            res.extend([root.val])
            res.extend(self.inorderTraversal(root.right))
        return res



class Solution(object):
    def inorderTraversal(self, root):
        nodeval = []
        curr = root
        stack = []

        while curr or len(stack) != 0 :
            if curr is None:
                curr = stack.pop()
                nodeval.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left

        return nodeval



























