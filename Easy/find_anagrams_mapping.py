# A = [12, 28, 46, 32, 50]
# B = [50, 12, 32, 46, 28]
# We should return
# [1, 4, 3, 2, 0]

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = {}
        for i,j in enumerate(B):
            d[j] = i
        return [d[x] for x in A]


