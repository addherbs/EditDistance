"""
Next Closest Time

Solution
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since i
"""

class Solution:
    def nextClosestTime(self, time: str) -> str:
        import itertools
        
        digits = set([int(x) for x in time if x != ':'])
        
        total_permuts = list(itertools.product(digits, repeat = 4))
        all_minutes = self.gen_all_minutes(total_permuts)
        return all_minutes[(all_minutes.index([time, self.str_to_minutes(time)]) + 1) % len(all_minutes)][0]
        
        
    def gen_all_minutes(self, total_permuts):
        
        val_ans = []
        
        for i in range(len(total_permuts)):
            m1, m2, s1, s2 = total_permuts[i]
            val = 0
            
            minutes = m1 * 10 + m2 
            seconds = s1 * 10 + s2
            
            if minutes < 24 and seconds < 60:
                val += minutes * 60
                val += seconds
                minutes = str(minutes if minutes > 9 else (str(0) + str(minutes)))
                seconds = str(seconds if seconds > 9 else (str(0) + str(seconds)))
                val_ans.append([minutes + ":" + seconds, val])
                                
        val_ans.sort(key = lambda x: x[1])
        
        return val_ans
            
            
        
    def str_to_minutes(self, s):
        return 60 * int(s[:2]) + int(s[3:])