class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n == 0): return False
        t = n
        while ( t > 3):
            t /= 3
        if (t == 3 or t == 1): return True
        else: return False