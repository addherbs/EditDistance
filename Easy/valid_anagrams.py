class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        d2 = {}
        for x in s:
            if (x in d1):
                d1[x] += 1
            else:
                d1[x] = 1
        for x in t:
            if (x in d2):
                d2[x] += 1
            else:
                d2[x] = 1
        if (len (d1) != len (d2)):
            return False
        else:
            for key, value in d1.items ():
                if key not in d2:
                    return False
                else:
                    if value != d2[key]:
                        return False

        return True