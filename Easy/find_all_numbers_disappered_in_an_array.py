class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if (not nums): return []

        d = set(nums)
        return [x for x in range(1,len(nums)+1) if (x not in d)]