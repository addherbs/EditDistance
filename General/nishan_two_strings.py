class Solution():
    def __init__(self):
        self.list = []

    def _calculate(self, input, output):
        if (len (input) == 0):
            if (output != '' and (output not in self.list) and len (output) > 1):
                self.list.append (output)
            return None
        else:
            self._calculate (input[1:], output)
            self._calculate (input[1:], output + input[0])

    def return_list(self, string):
        self._calculate (string, '')
        return self.list


def solution(S, T):

    if (len(S) == 1 and len(T) == 1):
        return S == T

    object = Solution()
    subsequence_list = object.return_list(S)
    if (T in subsequence_list):
        return 1
    else:
        return 0

print(solution("abcd", "abc"))