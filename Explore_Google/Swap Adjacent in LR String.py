"""
Swap Adjacent in LR String

Solution
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

 

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
Example 3:

Input: start = "LLR", end = "RRL"
Output: false
Example 4:

Input: start = "XL", end = "LX"
Output: true
Example 5:

Input: start = "XLLR", end = "LXLX"
Output: false
 

Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""

"""
         Key observations:
There are three kinds of characters, ‘L’, ‘R’, ‘X’.
Replacing XL with LX = move L to the left by one
Replacing RX with XR = move R to the right by one
If we remove all the X in both strings, the resulting strings should be the same.
        Additional observations:
Since a move always involves X, an L or R cannot move through another L or R.
Since anL can only move to the right, for each occurrence of L in the start string, its position should be to the same or to the left of its corresponding L in the end string.
"""

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        start_list = [[i, ch] for i, ch in enumerate(start) if ch != 'X']
        end_list = [[i, ch] for i, ch in enumerate(end) if ch != 'X']
        
        if len(start_list) != len(end_list): return False
        
        for i in range(len(start_list)):
            p, x = start_list[i]
            q, y = end_list[i]
            
            if x != y: return False
            
            if x == 'L' and p < q: return False
            
            if x == 'R' and p > q: return False
        
        return True
    