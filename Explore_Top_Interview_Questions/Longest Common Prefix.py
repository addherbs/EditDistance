"""
Longest Common Prefix

Solution
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        
        ans = strs[0]
        
        for i in range(1, len(strs)):
            compare = strs[i]
            
            j = 0
            for j in range(min(len(ans), len(compare))):
                if compare[j] == ans[j]:
                    j += 1
                else: break
            ans = compare[:j]
        
        return ans