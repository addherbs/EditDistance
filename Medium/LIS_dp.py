class Solution:
    def lengthOfLIS(self, nums):
        if (not nums): return 0

        dp = [1] * len (nums)
        res = 1
        for i in range (1, len (nums)):
            for j in range (0, i):
                if (nums[j] < nums[i]):
                    dp[i] = max (dp[i], dp[j] + 1)
                res = max (dp[i], res)

        return res