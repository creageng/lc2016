
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res += [root.val]
        return res


class Solution(object):
    def postorderTraversal(self, root):
        res = []
        unvisited = [root]
        while unvisited:
            node = unvisited.pop()
            if node:
                res.append(node.val)
                unvisited.append(node.left)
                unvisited.append(node.right)
        return res[::-1]

