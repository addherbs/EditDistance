class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for x in s:
            if (x in d):
                d[x] += 1
            else:
                d[x] = 0

        for x in s:
            if (d[x] == 0):
                return s.index (x)

        return -1