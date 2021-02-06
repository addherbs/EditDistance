"""
131. Palindrome Partitioning
Medium

2407

79

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        palindrome_map = set()
        self._recurse([], s, palindrome_map, ans)
        return ans
    
    def _recurse(self, current_list, remaining_string, palindrome_map, ans):
        
        if not remaining_string:
            return
        
        if self.is_palindrome(remaining_string, palindrome_map):
            ans.append(current_list + [remaining_string])
        
        for i in range(len(remaining_string)):
            current_string = remaining_string[0:i+1]
            
            if self.is_palindrome(current_string, palindrome_map):
                next_string = remaining_string[i+1:]
                current_list.append(current_string)
                self._recurse(list(current_list), next_string, palindrome_map, ans)
                current_list.pop()


    def is_palindrome(self, string, palindrome_map):
        if string in palindrome_map:
            return True
        if string == string[::-1]:
            palindrome_map.add(string)
            return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        dp = set()
        self.backtrack(s, 0, [], dp, ans)
        
        return ans
    
    def backtrack(self, s, start, cur_list, dp, ans):
        
        # if not s: return
        if start >= len(s):
            ans.append(list(cur_list))
        
        for i in range(start, len(s)):
            
            if s[i] == s[start] and (i-start <= 2 or (str(start+1) + str(i-1)) in dp ):
                dp.add(str(start)+str(i))
                cur_list.append(s[start:i+1])
                self.backtrack(s, i+1, cur_list, dp, ans)
                cur_list.pop()
                
