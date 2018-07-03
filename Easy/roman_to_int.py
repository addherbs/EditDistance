class Solution:
    def romanToInt(self, s):
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000

        }
        prio = {'IV': 4,
                'IX': 9,
                'XC': 90,
                'XL': 40,
                'CD': 400,
                'CM': 900
                }
        sum = 0
        i = 0
        while (i < len (s)):
            if (len (s[i:]) >= 2 and (s[i] + s[i + 1]) in prio):
                sum += prio[s[i] + s[i + 1]]
                i += 2
            else:
                sum += dict[s[i]]
                i += 1
        print (sum)
        return sum
