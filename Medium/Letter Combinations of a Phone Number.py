class Solution:
    def __init__(self):
        self.rtype = set ()
        self.map = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    def letterCombinations(self, digits):

        result = self._recurse (digits)
        print (result)
        return result

    def _recurse(self, digits):

        if (not digits): return []
        final = []
        res = self._recurse (digits[1:])

        for each_word in self.map[int (digits[0])]:
            if (res):
                for return_word in res:
                    final.append (each_word + return_word)
            else:
                final.append (each_word)

        return final