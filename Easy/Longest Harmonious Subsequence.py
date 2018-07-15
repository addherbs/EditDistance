import collections
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        p = collections.Counter (nums)

        ans = 0

        for num in nums:
            temp = 1
            if (num + 1 in p):
                ans = max (ans, p[num + 1] + p[num])

        print (p, ans)
        return ans