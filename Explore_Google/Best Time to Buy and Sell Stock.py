"""
Best Time to Buy and Sell Stock

Solution
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# O(N) Space complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        temp = [0] * len(prices)
        temp[0] = prices[0]
        for i in range(1, len(prices)):
            temp[i] = min(temp[i-1], prices[i])
        
        ans = 0
        right_max = 0
        for i in range(len(prices) - 1, -1, -1):
            right_max = max(prices[i], right_max)
            ans = max(ans, right_max - temp[i])
        
        return ans
        
        
# O(1) Space complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        left_min = float('inf')
        ans = 0
        
        for i in range(len(prices)):
            left_min = min(left_min, prices[i])
            ans = max(ans, prices[i] - left_min)
        return ans