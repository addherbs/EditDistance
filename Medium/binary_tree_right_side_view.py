# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root: return []
        return self.dfs(root)

    def dfs(self, parent):
        if not parent: return []
        left, right = [], []
        left += self.dfs(parent.left)
        right += self.dfs(parent.right)

        return [parent.val] + right + left[len(right):]
