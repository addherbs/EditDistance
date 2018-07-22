class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if (not nums or k == 0):
            return []
        if (len (nums) == 1 or k == 1):
            return nums
        if (k >= len (nums)):
            return [max (nums)]

        result = []
        current_max = max (nums[:k])
        result.append (current_max)
        index = nums.index (current_max)

        for x in range (1, len (nums) - k + 1):
            if (index == x - 1):
                current_max = max (nums[x:x + k])
                result.append (current_max)
                index = nums.index (current_max, x)
                # print("part 1 ==>> x: {}-> currentmax: {} -> index: {}, ->result: {}".format(x,current_max,index, result) )
            else:
                current_max = max (result[-1], nums[x + k - 1])
                result.append (current_max)
                index = nums.index (current_max, x)
                # print("part 2 ==>> x: {}-> currentmax: {} -> index: {}, ->result: {}".format(x,current_max,index, result) )

        print (result)
        return result