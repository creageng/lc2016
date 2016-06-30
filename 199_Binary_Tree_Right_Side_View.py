# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# For example:


# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        self.levelorder(root, 0, res)
        if res == []:
            return res
        
        val = []
        for e in res:
            val.append(e[-1])
        return val


    def levelorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.levelorder(root.left, level + 1, res)
            self.levelorder(root.right, level + 1, res)
 


class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]


# DFS-traverse the tree right-to-left, add values to the view whenever 
# we first reach a new record depth. This is O(n).
class Solution(object):
    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view


# Traverse the tree level by level and add 
# the last value of each level to the view. This is O(n).

class Solution(object):
    def rightSideView(self, root):
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view












    





