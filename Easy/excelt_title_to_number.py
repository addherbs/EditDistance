class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for x in s:
            result *= 26
            result += (ord (x) - 64)

        return result