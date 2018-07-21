class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_sum = max_sum = nums[0]

        for each in nums[1:]:
            current_sum = max (each, current_sum + each)
            max_sum = max (max_sum, current_sum)

        return max_sum