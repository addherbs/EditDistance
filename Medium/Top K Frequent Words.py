# from Queue import PriorityQueue
from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        count = Counter (words)
        candidates = list (count.keys ())
        print (count, candidates)
        candidates.sort (key=lambda w: (-count[w], w))
        print (candidates)

        return candidates[:k]