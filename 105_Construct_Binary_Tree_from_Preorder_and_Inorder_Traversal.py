
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Tree, array, dfs

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root






class Solution2(object):
    def buildTree(self, preorder, inorder):      
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootPos+1], inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:],inorder[rootPos+1:])
        return root