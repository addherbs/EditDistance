class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if (s == p): return True
        if (not p): return False

        check = lambda x, y: True if (s[x - 1] == p[y - 1] or p[y - 1] == ".") else False

        col = len (p) + 1;
        row = len (s) + 1

        dp = [[False] * col for _ in range (row)]

        dp[0][0] = True

        for i in range (1, col):
            if (p[i - 1] == "*"): dp[0][i] = dp[0][i - 2]

        for i in range (1, row):
            for j in range (1, col):
                if (check (i, j)):
                    dp[i][j] = dp[i - 1][j - 1]
                elif (p[j - 1] == "*"):
                    dp[i][j] = dp[i][j - 2]
                    if (check (i, j - 1)):
                        dp[i][j] = dp[i - 1][j] or dp[i][j]
                else:
                    dp[i][j] = False

        return dp[-1][-1]
