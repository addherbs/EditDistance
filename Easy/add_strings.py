class Solution (object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1, num2 = self.clean (num1, num2)

        l, carry, mod = '', 0, 0
        print (num1, num2)
        while (num1 or num2 or carry):
            if (num1):
                carry += int (num1[-1])
                num1 = num1[:-1]
            if (num2):
                carry += int (num2[-1])
                num2 = num2[:-1]
            carry, mod = divmod (carry, 10)
            l += str (mod)

        return l[::-1]

    def clean(self, s1, s2):
        l1 = len (s1)
        l2 = len (s2)
        while (l1 != l2):
            if (l1 < l2):
                l1 += 1
                s1 = '0' + s1
                # s1 += '0'
            else:
                l2 += 1
                s2 = '0' + s2
                # s2 += '0'

        return s1, s2