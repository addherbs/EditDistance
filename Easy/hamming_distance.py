class Solution (object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n1 = '{0:031b}'.format (x)
        n2 = '{0:031b}'.format (y)
        count = 0
        for i, j in zip (n1, n2):
            if (i != j):
                count += 1

        return count