from itertools import permutations
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self._check (nums)

    def _check(self, lit):
        if (len (lit) == 0):
            return []
        elif (len (lit) == 1):
            return [lit]
        else:
            l = []
            for i in range (len (lit)):
                curr = lit[i]
                extra = lit[:i] + lit[i + 1:]
                result = self._check(extra)
                for each in result:
                    l.append ([curr] + each)
            return l
