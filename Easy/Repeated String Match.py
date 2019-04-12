class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if (B in A): return 1
        if (set (A) != set (B)): return -1

        total = len (B) + 1
        i = 0
        init = A
        while (i < total):
            if (B in A): return i + 1
            A += init
            i += 1

        return -1