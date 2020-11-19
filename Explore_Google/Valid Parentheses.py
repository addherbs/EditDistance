"""
Valid Parentheses

Solution
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        dic = {"}" : "{", "]" : '[', ")": "("}
        stk.append(s[0])
        
        for i in range(1, len(s)):
            ch = s[i]
            if ch in dic:
                if stk:
                    last = stk.pop() 
                    if last != dic[ch]:
                        return False 
                else: return False
                
            else:
                stk.append(ch)
        
        return False if stk else True