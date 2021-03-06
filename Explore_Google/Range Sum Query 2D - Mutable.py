"""
Range Sum Query 2D - Mutable
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

# O(N * M) time complexity for sumRegion function
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.mat, self.m, self.n = [[]], 0, 0
        else:
            self.mat = [matrix[i][:] for i in range(len(matrix))]
            self.m, self.n = len(matrix), len(matrix[0])
        
    def update(self, row: int, col: int, val: int) -> None:
        if 0 <= row < self.m and 0 <= col < self.n:
            self.mat[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                ans += self.mat[i][j]
        return ans
            
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)


# O(N) time complexity for sumRegion function
class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.mat, self.m, self.n = [[]], 0, 0
        else:
            self.mat = [matrix[i][:] for i in range(len(matrix))]
            self.prefix_mat = [self.calc_prefix(row) for row in matrix]
            self.m, self.n = len(matrix), len(matrix[0])
        
    def update(self, row: int, col: int, val: int) -> None:
        if 0 <= row < self.m and 0 <= col < self.n:
            self.mat[row][col] = val
            self.prefix_mat[row] = self.calc_prefix(self.mat[row])
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            ans += (self.prefix_mat[i][col2]) - (0 if col1 == 0 else self.prefix_mat[i][col1 - 1])
        return ans

    def calc_prefix(self, row):
        prefix = []
        ans = 0
        for val in row:
            ans+= val
            prefix.append(ans)
        return prefix
