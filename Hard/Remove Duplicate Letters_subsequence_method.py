from collections import Counter
class Solution:
    def __init__(self):
        self.list = []
        self.len = None
        self.set = None

    def _calculate(self, input, output):

        if (len (output) > self.len): return None

        if (len (input) == 0):
            if (output != '' and (output not in self.list) and len (output) == self.len):
                self.list.append (output)
                print (self.list)
            return None
        else:
            self._calculate (input[1:], output)
            if (input[0] in self.set and input[0] not in output):
                self._calculate (input[1:], output + input[0])

    def removeDuplicateLetters(self, s):

        self.set = set (s)
        self.len = len (self.set)
        if (len (s) <= 1): return s

        self._calculate (s, '')
        temp_list = []

        self.set = set (s)
        p = Counter (set (s))

        for eachSub in self.list:
            if (Counter (eachSub) == p):
                temp_list.append (eachSub)

        temp_list.sort ()

        print (temp_list)
        return temp_list[0]

