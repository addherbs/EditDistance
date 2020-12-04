"""
Convert Sorted Array to Binary Search Tree

Solution
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    
        return self.gen_BST(nums, 0, len(nums) - 1)
    
    
    def gen_BST(self, nums, left, right):
        if not nums or left > right: return None
        mid = left + (right - left)  // 2
        
        node = TreeNode(nums[mid])
        node.left = self.gen_BST(nums, left, mid - 1)
        node.right = self.gen_BST(nums, mid + 1, right)
        
        return node
