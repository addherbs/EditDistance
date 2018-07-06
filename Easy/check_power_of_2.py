class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return True if (bin (n)[2:].count ("1") == 1 and n > 0) else False