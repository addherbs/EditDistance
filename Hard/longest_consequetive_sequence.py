class Solution (object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            if (x not in d):
                d[x] = set ()
            if (x - 1 in d):
                d[x - 1].add (x)
                d[x].add (x - 1)
            if (x + 1 in d):
                d[x + 1].add (x)
                d[x].add (x + 1)
        high = 0
        for i, j in d.items ():
            temp = [i]
            visited = set ()
            while (temp):
                p = temp.pop ()
                if (p in visited and len (temp) == 0):
                    break
                elif (p in visited and len (temp) > 0):
                    continue
                else:
                    visited.add (p)
                    if (p in d):
                        temp += [each for each in d[p]]
                        del d[p]
            if (len (visited) > high):
                high = len (visited)

        return high
