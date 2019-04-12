class Solution:
    def myPow(self, x, n):
        if (n < 0):
            x = 1 / x
            n = -1 * n
        return self.pow (x, n)

    def pow(self, x, n):
        if (n == 0):
            return 1.0
        else:
            half = self.pow (x, n // 2)
            if (n % 2 == 0):
                return half * half
            else:
                return half * half * x