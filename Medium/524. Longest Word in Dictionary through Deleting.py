"""
524. Longest Word in Dictionary through Deleting
Medium

353

186

Favorite

Share
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""

from copy import deepcopy
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        main_dic = dict()
        for i,ch in enumerate(s):
            if ch not in main_dic:
                main_dic[ch] = [i]
            else:
                main_dic[ch].append(i)
        
        result = []
        for word in d:
            dic = deepcopy(main_dic)
            currentIndex = -1
            for ch in word:
                if ch not in dic:
                    break
                else:
                    char_present = False
                    for ind in dic[ch]:
                        if ind > currentIndex:
                            currentIndex = ind
                            char_present = True
                            break
                    if not char_present:
                        break
            else:
                result.append(word)
        
        if not result: return ""
        
        max_len = max([len(res) for res in result])
        return list(sorted([res for res in result if len(res) == max_len]))[0]
        
                