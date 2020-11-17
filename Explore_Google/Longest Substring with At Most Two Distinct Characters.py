"""

Longest Substring with At Most Two Distinct Characters

Solution
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        from collections import defaultdict
        
        if len(set(s)) <= 2: return len(s)
        
        sub_dict = defaultdict(int)
        l, r = 0, 0
        max_sub = 0
        
        k = 2
        
        while r < len(s):
            
            sub_dict[s[r]] += 1
            
            if len(sub_dict) == k:
                max_sub = max(max_sub, r - l + 1)
            
            
            while len(sub_dict) > k:
                sub_dict[s[l]] -= 1
                if sub_dict[s[l]] == 0:
                    sub_dict.pop(s[l])
                l += 1
            
            r += 1
        return max_sub