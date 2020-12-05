"""
Power of Three

Solution
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you do it without using any loop / recursion?
"""


# Loop solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        p = 3
        while p <= n:
            if p == n:
                return True
            p *= 3
        return False
        
        
        
        
        
# Solution using log without loop
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        import math
        
        temp = math.log(n) / math.log(3)
        nearest_int = round(temp)
        epsilon = 0.00000000001 # This is a double error called epsilon in programming/ machine
        if abs(temp-nearest_int) < epsilon:
            if nearest_int % 1 == 0:
                return True
        return False
        
        
        
# Using Mathematics
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # maximum value of n that is also a power of three is 1162261467 and less than 2**31 - 1
        return n > 0  and 3 ** 19 % n == 0