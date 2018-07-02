class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums or min (nums) == 1):
            return 0

        if (len (nums) == 1 and nums[0] != 0):
            return nums[0] - 1
        if (len (nums) == 1 and nums[0] == 0):
            return 1

        d = {}
        for x in nums:
            d[x] = 1

        for x in range (min (nums), max (nums) + 2):
            if (x not in d):
                return x

