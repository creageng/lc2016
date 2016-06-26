# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res += [root.val]
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res




class Solution(object):
    def preorderTraversal(self, root):

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

        # if not root:
        #     return []

        # stack = [root]
        # res = []

        # while stack:
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)

        # return res














