import sys


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0

        for j in range (len (coins)):
            for i in range (1, amount + 1):
                if (i >= coins[j]):
                    dp[i] = min (dp[i], 1 + dp[i - coins[j]])

        return -1 if dp[-1] == sys.maxsize else dp[-1]