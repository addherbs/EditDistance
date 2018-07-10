class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S
        k = K
        s = s.upper().replace("-", "")
        count = 0
        c = ""
        print(s, " ", k)
        for i in s[::-1]:
            print (i)
            if (count == k):
                count = 1
                c += "-" + i
            else:
                c += i
                count += 1

        return c[::-1]