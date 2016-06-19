#  Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Subscribe to see which companies asked this question


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.n1 = self.n2 = None
        # prev指针用来比较中序遍历中相邻两个值的大小关系
        self.prev = None
        self.Find2Nodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val

    def Find2Nodes(self, root):
        if root:
            self.Find2Nodes(root.left)

            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if self.n1 is None:
                    # first encountered broken pairs
                    self.n1 = self.prev
            self.prev = root
            ## updating current node            
            self.Find2Nodes(root.right)