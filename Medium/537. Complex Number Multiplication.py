# 537. Complex Number Multiplication
# Medium
#
# Given two strings representing two complex numbers.
#
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
#
# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
# Note:
#
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        r1, c1 = self.simplify(a)
        r2, c2 = self.simplify(b)

        real = (r1 * r2) + (-1) * (c1 * c2)
        complex = (r1 * c2) + (r2 * c1)

        complex_number = str(real) + "+" + str(complex) + "i"

        return complex_number

    def simplify(self, complex_number):
        sep = complex_number.find("+")
        real = int(complex_number[:sep])
        complex = int(complex_number[sep + 1:-1])
        return real, complex


sol = Solution()

tests = [["1+1i", "1+1i", "0+2i"], ["1+-1i", "1+-1i", "0+-2i"]]

for test in tests:
    ans = test[2]
    value = sol.complexNumberMultiply(test[0], test[1])
    print ("result: ", ans == value, ans, value)
