"""
654. Maximum Binary Tree
Medium

1159

145

Favorite

Share
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.dic = {}
        self.levels = defaultdict(list)
     
    def _calculate(self, nums, node):
        max_index = nums.index(max(nums))
        max_value = nums[max_index]
        node.val = max_value
        
        if nums[:max_index]:
            node.left = self._calculate(nums[:max_index], TreeNode(None))
        if nums[max_index + 1:]:
            node.right = self._calculate(nums[max_index + 1:], TreeNode(None))
        
        return node
        
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if not nums: return
        max_index = nums.index(max(nums))
        max_value = nums[max_index]
        root = TreeNode(max_value)
        
        if nums[:max_index]:
            root.left = self._calculate(nums[:max_index], TreeNode(None))
        if nums[max_index + 1:]:
            root.right = self._calculate(nums[max_index + 1:], TreeNode(None))
        
        return root
