# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        string = self.preorder (root).strip ()
        print (string)
        return string

    def preorder(self, node):
        if not node:
            return "*"

        string = ""
        string += str (node.val) + " "
        string += self.preorder (node.left) + " "
        string += self.preorder (node.right) + " "

        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        temp = []
        data = data.split ()
        for each in data:
            if (each == "*"):
                temp.append (None)
            else:
                temp.append (int (each))

        tag = -1
        # print ("de temp", temp)

        result, tag = self.gen_tree (temp, tag)
        return result

    def gen_tree(self, data, tag):
        tag += 1

        if (tag >= len (data) or data[tag] == None):
            return None, tag

        node = TreeNode (data[tag])
        node.left, tag = self.gen_tree (data, tag)
        node.right, tag = self.gen_tree (data, tag)

        return node, tag

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))