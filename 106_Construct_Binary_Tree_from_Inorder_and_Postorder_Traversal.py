# Given inorder and postorder traversal of a tree, construct the binary tree.




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Memory Limit Exceeded

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        # root = TreeNode(postorder.pop())
        # rootPos = inorder.index(root.val)
        # root.left = self.buildTree(inorder[:rootPos], postorder[0:rootPos])
        # root.right = self.buildTree(inorder[rootPos+1:], postorder[rootPos:-1])

        root = TreeNode(postorder.pop())
        rootPos = inorder.index(root.val)
        
        root.right = self.buildTree(inorder[rootPos+1:], postorder)
        root.left = self.buildTree(inorder[:rootPos], postorder)

        return root

