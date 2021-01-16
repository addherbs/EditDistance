"""
Pascal's Triangle

Solution
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        ans = [[1]]
        for i in range(1, numRows):
            temp = [ans[-1][0]]
            for j in range(len(ans[-1]) - 1):
                temp.append(ans[-1][j] + ans[-1][j+1])
            temp.append(ans[-1][-1])
            ans.append(temp)
        return ans