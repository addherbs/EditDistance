# 227. Basic Calculator II
# Medium
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5

class Solution:

    def extend(self, char, index, string):
        p = index + 1

        while p < len(string) and string[p].isnumeric():
            char += string[p]
            p += 1

        index = p - 1

        return index, char

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        operators = ""
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isnumeric():
                i, ch = self.extend(ch, i, s)
                stack.append(int(ch))
            elif ch in ['+', '-']:
                operators += ch
            elif ch == "*":
                i += 1
                next_ch = s[i]
                i, next_ch = self.extend(next_ch, i, s)
                stack.append(stack.pop() * int(next_ch))
            elif ch == "/":
                i += 1
                next_ch = s[i]
                i, next_ch = self.extend(next_ch, i, s)
                stack.append(stack.pop() // int(next_ch))

            i += 1

        if not operators:
            return stack.pop()
        else:
            stack.reverse()
            i = 0
            while i < len(operators):
                ch = operators[i]
                if ch == "+":
                    stack.append(stack.pop() + stack.pop())
                else:
                    stack.append(stack.pop() - stack.pop())
                i += 1
            return stack.pop()


s = Solution()


tests = [["3+2*2", 7], [" 3/2 ", 1], [" 3+5 / 2 ", 5], ["42", 42], ["1*2-3/4+5*6-7*8+9/10", -24]]

for i in range (len(tests)):
    ans = tests[i][1]
    value = s.calculate(tests[i][0])
    print("result ", ans, value)
    print (ans == value)
