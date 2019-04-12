import collections
class Solution (object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = collections.Counter (s)
        odd = 0
        for value in d.values ():
            if (value % 2 != 0): odd += 1

        if (odd <= 1):
            return True
        else:
            return False
