class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (not nums or max(nums) < 1): return 1
        d = set(nums)
        for i in range (1, max(nums) + 2):
            if (i not in d):
                return i