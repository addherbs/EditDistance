class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        return self._cal (matrix)

    def _cal(self, mat):
        if (not mat): return mat
        l = [*mat.pop (0)]
        l = l + self._cal ([*zip (*mat)][::-1])
        return l