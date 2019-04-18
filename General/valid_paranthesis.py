class Solution (object):
    def isValid(self, s):

        s = str (s)
        if (len (s) == 1):
            return False

        list = []
        dict = {']': '[', '}': '{', ')': '('}
        for x in s:
            # print (list)
            if (x is '(' or x is '[' or x is '{'):
                list.append (x)
            elif (x is ')' or x is ']' or x is '}'):
                if (len (list) >= 1):
                    if (dict[x] == list[-1]):
                        list.pop ()
                    else:
                        return False
                else:
                    return False

        if (len (list) == 0):
            return True
        else:
            return False
