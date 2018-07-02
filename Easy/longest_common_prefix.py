class Solution (object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (not strs):
            return ""
        if (len (strs) == 1):
            return strs[0]
        s = strs[0]
        for i in range (1, len (strs)):
            s = self.common_prefix (strs[i], s)
        return s

    def common_prefix(self, s1, s2):
        s = ""
        ran = min (len (s1), len (s2))
        for i in range (ran):
            if (s1[i] != s2[i]):
                break
            s += s1[i]
        return s