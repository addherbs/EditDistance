"""
Binary Tree Level Order Traversal

Solution
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        self.dfs(root, 0, ans)
        return ans
    
    
    def dfs(self, node, level, ans):
        if not node: return
        if level > len(ans) - 1:
            ans.append([node.val])
        else:
            ans[level].append(node.val)
        if node.left:
            self.dfs(node.left, level + 1, ans)
        if node.right:
            self.dfs(node.right, level + 1, ans)