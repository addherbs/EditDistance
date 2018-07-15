class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if (x < 0):
            sign = -1
            x = abs (x)

        num = 0
        while (x > 0):
            x, r = divmod (x, 10)
            num = num * 10 + r

        num = num * sign
        return num if (-1 * 2 ** 31 < num < 2 ** 31) else 0