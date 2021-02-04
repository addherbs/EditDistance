#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#


def check(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_col_list = [set(), set()]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_col_list[0].add(i)
                row_col_list[1].add(j)

    for each_row in row_col_list[0]:
        for i in range(cols):
            matrix[each_row][i] = 0

    for each_col in row_col_list[1]:
        for i in range(rows):
            matrix[i][each_col] = 0
