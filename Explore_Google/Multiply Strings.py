"""
Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        ans = 0
        for i in range(len(num1) - 1, -1, -1):
            multi_factor = 10**(abs(i - (len(num1) - 1)))
            carry = 0
            temp = []

            for j in range(len(num2) - 1, -1, -1):
                carry, r = divmod(int(num2[j]) * int(num1[i]) + carry, 10)
                temp.append(r)
            
            if carry:
                temp.append(carry)
            
            val = 0
            while temp:
                val = val * 10 + temp.pop()
            ans += val * multi_factor
            
        return str(ans)