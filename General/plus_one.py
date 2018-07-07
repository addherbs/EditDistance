class Solution (object):
    def plusOne(self, digits):

        if (len (digits) == 0):
            return digits

        sum = 0

        for x in digits:
            sum = sum * 10 + x

        sum += 1

        return [int (x) for x in str (sum)]