# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.output = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self._check (root)
        return self.output

    def _check(self, root):
        if (root == None):
            return None
        else:
            self._check (root.left)
            self.output.append (root.val)
            self._check (root.right)
