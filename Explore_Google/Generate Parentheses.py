"""
Generate Parentheses

Solution
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def recurse(left, right, current):
            if left == right == n:
                ans.append(current)
                return
            
            if left > n or right > n or right > left:
                return
            
            if left > right:
                recurse(left, right + 1, current + ")")
            
            if left < n:
                recurse(left + 1, right, current + "(")
        
        recurse(0, 0, "")
        
        return ans