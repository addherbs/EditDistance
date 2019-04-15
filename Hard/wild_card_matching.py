import re


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        while ("**" in p):
            p = p.replace ("**", "*")

        row = len (s) + 1;
        col = len (p) + 1
        dp = [[False] * col for _ in range (row)]
        dp[0][0] = True

        if (p and p[0] == "*"): dp[0][1] = True

        for i in range (1, row):
            for j in range (1, col):
                if (s[i - 1] == p[j - 1] or p[j - 1] == "?"):
                    dp[i][j] = dp[i - 1][j - 1]
                elif (p[j - 1] == "*"):
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[-1][-1]