"""
Longest Increasing Path in a Matrix
Hard

2437

42

Add to List

Share
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        ans = 0

        m = len(matrix)
        n = len(matrix[0])
        mat = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                    ans = max(ans, self.calc(i, j, matrix, mat, m, n))
        return ans

    def calc(self, i, j, matrix, mat, m, n):
        if mat[i][j] == "#": return 0
        if mat[i][j]: return mat[i][j]

        nxt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        mat[i][j] = "#"
        for each in nxt:
            x, y = i + each[0], j + each[1]
            if (0 <= x < m and 0 <= y < n) and matrix[x][y] > matrix[i][j]:
                mat[i][j] = max(1 if mat[i][j] == "#" else mat[i][j] , self.calc(x, y, matrix, mat, m, n))

        mat[i][j] = 1 if mat[i][j] == "#" else mat[i][j] + 1
        return mat[i][j]
