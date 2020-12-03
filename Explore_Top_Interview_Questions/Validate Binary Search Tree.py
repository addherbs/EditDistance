"""
Validate Binary Search Tree

Solution
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Using Recursion and validating from bottom to top

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        
        low, high, ans = self.validate(root)
        
        return ans


    def validate(self, node):
        if not node: return float('-inf'), float('inf'), True
        
        if not node.left and not node.right: return node.val, node.val, True
        
        valid = True
        
        if not node.left:
            left_low, left_high = float('-inf'), float('-inf')
        else:
            left_low, left_high, valid = self.validate(node.left)
            
        if not node.right:
            right_low, right_high = float('inf'), float('inf')
        else:
            right_low, right_high, valid = self.validate(node.right)
        
        if valid and left_high < node.val < right_low:
            left_low = node.val if left_low == float('-inf') else left_low
            right_high = node.val if right_high == float('inf') else right_high
            return left_low, right_high, True
        else:
            return float('-inf'), float('inf'), False
        

