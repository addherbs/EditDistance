class Solution:
    def lengthLongestPath(self, input):

        d = {-1: 0}
        value = 0

        for each in input.splitlines ():
            level = each.count ("\t")
            d[level] = d[level - 1] + len (each) - level
            if ("." in each):
                value = max (value, d[level] + level)

        print (d)

        return value