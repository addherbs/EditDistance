"""
Letter Combinations of a Phone Number

Solution
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2': set("abc"),
            '3': set("def"), 
            '4': set("ghi"), 
            '5': set("jkl"), 
            '6': set("mno"), 
            '7': set("pqrs"), 
            '8': set("tuv"), 
            '9': set("wxyz"), 
        }
        
        def recurse(number):
            if not number: return []
            current = list(dic[number[0]])
            if not number[1:]: return current
            answer = []
            for next_value in recurse(number[1:]):
                for each in current:
                    answer.append(each+next_value)
            return answer
        
        return recurse(digits)