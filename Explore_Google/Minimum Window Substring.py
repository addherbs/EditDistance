"""
Minimum Window Substring

Solution
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
 

Follow up: Could you find an algorithm that runs in O(n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t or len(t) > len(s): return ""
        
        from collections import Counter, defaultdict
        ans = [len(s)+1, -1, -1]
        l, r = 0, 0
        windows_dict = defaultdict(int)
        t_dict = Counter(t)
        formed = 0
        
        while r < len(s):
            ch = s[r]
            
            windows_dict[ch] += 1
            
            if ch in t_dict and windows_dict[ch] == t_dict[ch]:
                formed += 1

            if formed == len(t_dict):
                
                while formed == len(t_dict):
                    if r - l + 1 < ans[0]:
                        ans[0], ans[1], ans[2] = r - l + 1, l, r
                    
                    windows_dict[s[l]] -= 1
                    if s[l] in t_dict and t_dict[s[l]] > windows_dict[s[l]]:
                        formed -= 1
                    l += 1
            r += 1
        
        return s[ans[1]:ans[2] + 1] if ans[1] != -1 else "" 
    