"""
Strobogrammatic Number II
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dic = {}
        dic[0] = [""]
        dic[1] = ["0", "1", "8"]
        dic[2] = ["11","69","88","96"]
        inside = ["11","69","88","96", "00"]
        if n <= 2: return dic[n]
        
        def recurse(num, count = 1):
            if num <= 1: return dic[num]
            if count == 1:
                temp = dic[2]
            else:
                temp = inside[:]
            answer = []
            
            values = recurse(num - 2, count + 1)
            
            for each in temp:
                for val in values:
                    answer.append(each[0] + val + each[1])
            
            return answer
            
        return recurse(n)
                