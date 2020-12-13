"""
Binary Tree Maximum Path Sum

Solution
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
 

Constraints:

The number of nodes in the tree is in the range [0, 3 * 104].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        c_max, total = self._recurse(root)
        
        return total
        
    def _recurse(self, node):
        
        if not node:
            return float('-inf'), float('-inf')
        
        left_max, total_max1 = self._recurse(node.left)
        right_max, total_max2 = self._recurse(node.right)
        
        current_max = max(node.val, node.val+right_max, node.val + left_max)
        return current_max, max(total_max1, total_max2, current_max, node.val + left_max + right_max)