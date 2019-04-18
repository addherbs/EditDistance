class Solution (object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        final = 0
        count = 1
        while (num2):
            val = self.cal (num1, int (num2[-1]))
            final += val * count
            count *= 10
            num2 = num2[:-1]

        # return str(int(num1) * int(num2))

        return str (final)

    def cal(self, num, digit):
        d, carry = 0, 0
        n = ''

        while (num or carry):
            if (num):
                carry = carry + (int (num[-1]) * digit)
                num = num[:-1]
            carry, d = divmod (carry, 10)
            n += str (d)

        return int (n[::-1])