"""
Climbing Stairs

Solution
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""


# Fibonacci sequence, O(n) time
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        a = 1
        b = 1
        c = 2
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c
        
        
        
# Fibonacci formula, O(log(n))
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = 5 ** (1/2)
        n = n + 1
        return int(( ( (1 + sqrt5)/2 ) ** n - ( (1 - sqrt5)/2 ) ** n ) / sqrt5)
