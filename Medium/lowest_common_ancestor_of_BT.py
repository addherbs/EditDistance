# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.p = None
        self.q = None
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.lca = self._recurse (root, p.val, q.val)

        return self.lca

    def _recurse(self, parent, p, q):

        if ((self.p and self.q) or not parent):
            return None

        if (parent.val is p):
            self.p = p
            return parent

        if (parent.val is q):
            self.q = q
            return parent

        left = self._recurse (parent.left, p, q)
        right = self._recurse (parent.right, p, q)

        if (left and right):
            return parent
        elif (left):
            return left
        elif (right):
            return right
        else:
            return None