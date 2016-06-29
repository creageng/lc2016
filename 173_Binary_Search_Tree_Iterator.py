# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

# Credits:


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushLeft(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack
        

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# A node may or may not have a right subtree.

# If it has, then we know the next smallest element is in the right subtree, so we need to do the same thing(the while loop) to the right subtree, you can think of this as the 'recursion';

# if no right subtree, the next element is the stack top.


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


# http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

class BSTIterator(object):
    def __init__(self, root):
        self.last = root
        while self.last and self.last.right:
            self.last = self.last.right

        self.curr = None
        self.g = self.iterate(root)

    def hasNext(self):
        return self.curr is not self.last

    def next(self):
        return next(self.g)

    def iterate(self, node):
        if node is None:
            return

        for x in self.iterate(node.left):
            yield x

        self.curr = node
        yield node.val
        
        for x in self.iterate(node.right):
            yield x






















