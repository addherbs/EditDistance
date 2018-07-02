class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = len (nums) // 2
        d = {}
        for x in nums:
            if (x not in d):
                d[x] = 1
            else:
                d[x] += 1

            if (d[x] > maj):
                return x