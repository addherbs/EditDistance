class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if (len (nums) != 1):
            total = 0
            for i, j in enumerate (nums):
                if (j == 0):
                    total += 1
                else:
                    nums[i - total] = j

            for x in range (len (nums) - total, len (nums)):
                print (" lol ")
                nums[x] = 0