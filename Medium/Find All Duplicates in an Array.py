class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num in nums:
            sign = abs (num) - 1

            if (nums[sign] < 0):
                result.append (abs (num))
            nums[sign] = nums[sign] * -1

        return result