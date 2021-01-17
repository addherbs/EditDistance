"""
77. Combinations
Medium

1803

74

Add to List

Share
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(current, start):
            if len(current) == k:
                ans.append(list(current))
                return
            for i in range(start, n+1):
                current.append(i)
                
                backtrack(current, i + 1)

                current.pop()
                
        backtrack([], 1)
        
        return ans
