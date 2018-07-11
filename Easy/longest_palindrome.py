import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = collections.Counter (s)
        odd = 0
        for value in d.values ():
            if (value % 2 != 0): odd += 1

        if (odd >= 1):
            return len (s) - odd + 1
        else:
            return len (s)
