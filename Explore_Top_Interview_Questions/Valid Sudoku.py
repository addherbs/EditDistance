"""
Valid Sudoku

Solution
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
"""


# 3 set solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board: return False 
        
        def calc_range(x):
            return x // 3
        
        def calc_box(x, y):
            return calc_range(x) * 3 + calc_range(y) 
        
        
        m, n = len(board), len(board[0])
        
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        box = [set() for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                val = board[i][j]
                if val != ".":

                    box_num = calc_box(i, j)
                    if val in rows[i] or val in cols[j] or val in box[box_num]:
                        return False
                    rows[i].add(val)
                    cols[j].add(val)
                    box[box_num].add(val)
        return True