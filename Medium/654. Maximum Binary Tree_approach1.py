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

""" 									Approach 1
from collections import defaultdict

class Solution:
    
    def __init__(self):
        self.dic = {}
        self.levels = defaultdict(list)
        
    def _calculate(self, temp, level):
        if not temp:
            return
        level += 1
        max_index = temp.index(max(temp))
        max_value = temp[max_index]
        self.levels[level].append(max_value)
        self.dic[max_value] = [None, None]
        if temp[:max_index]:
            self.dic[max_value][0] = self._calculate(temp[:max_index], level)
        if temp[max_index + 1:]:
            self.dic[max_value][1] = self._calculate(temp[max_index + 1:], level)
        return max_value
        
    def _construct(self, node):
        if not node:
            return
        current_left = self.dic[node.val][0]
        current_right = self.dic[node.val][1]
        if isinstance(current_left, int) :
            node.left = TreeNode(current_left)
            self._construct(node.left)
        if isinstance(current_right, int) :
            node.right = TreeNode(current_right)
            self._construct(node.right)
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if not nums: return
        
        self._calculate(nums[:], -1)
        root = TreeNode(self.levels[0][0])
        temp = root
        self._construct(temp)
        
        return root
    
"""