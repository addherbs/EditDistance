class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        if (not s): return 0
        n = len (s)

        t = s[::-1]

        dp = [[1] * (n) for _ in range (n)]

        # for i in range (n): dp[i][i] = 1

        for i in range (2, n + 1):
            for j in range (n - i + 1):

                length = j + i - 1

                if (i == 2 and s[j] == s[length]):
                    dp[j][length] = 2
                elif (s[j] == s[length]):
                    dp[j][length] = dp[j + 1][length - 1] + 2
                else:
                    dp[j][length] = max (dp[j + 1][length], dp[j][length - 1])
                    # print (dp)
        return dp[0][-1]