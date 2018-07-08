import collections

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        p = dict (collections.Counter (S))
        ans = 0
        for c in J:
            if (c in p):
                ans += p[c]

        return ans