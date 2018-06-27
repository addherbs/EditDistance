class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for x in range(1, len (prices)):
            if (prices[x] > prices[x - 1]):
                result += prices[x] - prices[x - 1]

        return result