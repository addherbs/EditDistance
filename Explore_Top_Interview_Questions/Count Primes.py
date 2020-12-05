"""
Count Primes
Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
"""



class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2: return 0
        if n == 3: return 1 
        
        nums = [1] * n

        for i in range(2, (n+1) //2):
            j = i + i
            while j < n :
                nums[j] = 0
                j += i

        return nums.count(1) - 2