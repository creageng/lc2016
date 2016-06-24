# given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,

#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = 12 + 13 = 25.

# dfs, tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        if root == None:
            return 0
        else:
            self.dfs(root, 0)
            return self.res


    def dfs(self, root, pathVal):
        if root.left is None and root.right is None:
            self.res += pathVal * 10 + root.val

        else:
            if root.left:
                self.dfs(root.left, pathVal * 10 + root.val)

            if root.right:
                self.dfs(root.right, pathVal * 10 + root.val)
                



# dfs + stack
class Solution(object):
# dfs + stack

    def sumNumbers(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
    
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
    
                if node.right:
                    stack.append((node.right, value * 10 + node.right.val))
    
                if node.left:
                    stack.append((node.left, value * 10 + node.left.val))
        return res


#bfs + queue
class Solution(object):
    def sumNumbers(self, root):
        if not root:
            return 0

        queue, res = collections.deque([(root, root.val)]), 0

        while queue:
            node, value = queue.popleft()

            if node:
                if not node.left and not node.right:
                    res += value

                if node.left:
                    queue.append((node.left, value * 10 + node.left.val))

                if node.right:
                    queue.append((node.right, value * 10 + node.right.val))

        return res


# recursively

class Solution(object):
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root,0)
        return self.res

    def dfs(self, root, value):
        if root:
            self.dfs(root.left, value * 10 + root.val)
            self.dfs(root.right, value * 10 + root.val)

            if not root.left and not root.right:
                self.res += value * 10 + root.val






























