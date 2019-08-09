"""
1038. Binary Search Tree to Greater Sum Tree
Medium

228

33

Favorite

Share
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
 

Note:

The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.inorder = []
        self.new_values = {}
        self.sum = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        temp = root
        self._inorder(temp)
        new_values = self.calculate_new_values()
        temp = root
        self.update_new_values(temp)
        return root
    
    def _inorder(self, node):
        if not node:
            return
        if node.left:
            self._inorder(node.left)
        self.inorder.append(node.val)
        if node.right:
            self._inorder(node.right)
        
    def calculate_new_values(self):
        self.sum = sum(self.inorder)
        current_total = 0
        for each in self.inorder:
            self.new_values[each] = self.sum - current_total
            current_total += each
        
    def update_new_values(self, node):
        if not node:
            return
        node.val = self.new_values[node.val]
        if node.left:
            self.update_new_values(node.left)
        if node.right:
            self.update_new_values(node.right)