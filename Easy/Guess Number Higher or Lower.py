import random


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution (object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        initial = random.randint (low, high)
        while (1):
            value = guess (initial)
            if (value == 0):
                return initial
            elif (value == -1):
                high = initial
            else:
                low = initial

            initial = random.randint (low, high)