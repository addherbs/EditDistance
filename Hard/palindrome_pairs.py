class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        palin = lambda x: x == x[::-1]

        d = {x: i for i, x in enumerate (words)}
        res = []

        for value, key in d.items ():
            word_len = len (value)

            for i in range (word_len + 1):
                prif = value[:i]
                suff = value[i:]

                if (palin (prif)):
                    rev = suff[::-1]
                    if (rev in d and rev != value): res.append ([d[rev], key])

                if (palin (suff) and i != word_len):
                    rev = prif[::-1]
                    if (rev in d and rev != value): res.append ([key, d[rev]])

        return res