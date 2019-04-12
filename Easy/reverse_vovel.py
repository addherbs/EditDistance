class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vovel = set (['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        temp = []
        s = list (s)
        for c in s:
            if c in vovel: temp.append (c)
        print (temp)
        temp = temp[::-1]
        print (temp)
        for i, c in enumerate (s):
            if c in vovel: s[i] = temp.pop (0)
        print (temp)
        return "".join (s)
