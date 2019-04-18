import collections

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hT = collections.Counter (nums)
        result = sorted (hT, key=hT.get, reverse=True)[:k]

        return result