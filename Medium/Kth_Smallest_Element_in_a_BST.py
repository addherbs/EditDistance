# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.min = None
        self.k = None
        self.inorder = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k

        self._recurse (root)
        self.min = self.inorder[k - 1]
        return self.min

    def _recurse(self, node):
        if (node == None or len (self.inorder) == self.k):
            return
        else:
            self._recurse (node.left)
            self.inorder.append (node.val)
            self._recurse (node.right)
