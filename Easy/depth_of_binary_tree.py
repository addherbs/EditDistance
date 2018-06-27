class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.check (root, 1)

    def check(self, parent, value):
        if (parent is None):
            return value - 1
        else:
            return max (self.check (parent.left, value + 1), self.check (parent.right, value + 1))