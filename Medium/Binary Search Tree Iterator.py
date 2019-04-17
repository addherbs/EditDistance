# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator (object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.head = root
        self.inorderList = []
        self.inorder (root)
        self.current = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        if (self.current < len (self.inorderList)): return True

    def next(self):
        """
        :rtype: int
        """
        current = self.inorderList[self.current]
        self.current += 1
        return current

    def inorder(self, node):

        return self._inorder (node)

    def _inorder(self, node):
        if (not node): return
        self._inorder (node.left)
        self.inorderList.append (node.val)
        self._inorder (node.right)


        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())