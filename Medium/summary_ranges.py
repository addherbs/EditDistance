class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        tag = 0
        if (not nums): return []
        if (len (nums) == 1): return [str (nums[0])]
        res = []

        for i in range (1, len (nums)):
            if (nums[i] - 1 == nums[i - 1]):
                continue
            else:
                if (tag != i - 1):
                    res.append (str (nums[tag]) + "->" + str (nums[i - 1]))
                else:
                    res.append (str (nums[tag]))
                tag = i

        if (nums[-1] - 1 == nums[-2]):
            res.append (str (nums[tag]) + "->" + str (nums[-1]))
        else:
            res.append (str (nums[-1]))

        return res