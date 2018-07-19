from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s):

        self.set = set (s)
        self.len = len (self.set)
        if (len (s) <= 1): return s

        counter, visited, stack = Counter (s), set (), []

        for each in s:
            counter[each] -= 1

            if (each in visited): continue

            visited.add (each)

            while (stack and stack[-1] > each and counter[stack[-1]] >= 1):
                visited.remove (stack.pop ())

            stack.append (each)

        return "".join (stack)