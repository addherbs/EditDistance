"""
Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true
"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic = {
            '6': '9',
            '0': '0',
            '1': '1',
            '8': '8',
            '9': '6'
        }
        
        l, r = 0, len(num) - 1
        
        while l <= r:
            lc, rc = num[l], num[r]
            if l == r and lc not in dic: return False
            else:
                if  lc not in dic or rc not in dic or dic[lc] != rc: return False
            l += 1
            r -= 1
            
        return True