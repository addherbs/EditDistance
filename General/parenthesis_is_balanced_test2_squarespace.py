import sys


def is_balanced(input):
    input = str (input)

    list = []
    dict = {']': '[', '}': '{', ')': '(', '>': '<'}
    i = 0
    print ("\'abc'", )
    print(len(input))
    while (i < len (input)):
        x = input[i]
        if (x == "\\"):
            i += 1
        elif x is "'":
            print (i, input[i], "into ' ")
            next_group = input.find ("'", i + 1)
            if (next_group == -1): return False
            i = next_group
            print(i, input[i])
            if (i == len (input) - 1): return True
            # i += 1
            # if (i >= len (input)): return False
            # while (input[i] != "'"):
            #     i += 1
            #     if (i == len (input) - 1): return True
            #     if (i >= len (input)): return False

        elif x is '"':
            print (i, input[i], 'into " ')
            next_group = input.find ('"', i + 1)
            if (next_group == -1): return False
            i = next_group
            if (i == len (input) - 1): return True
            print (i)
            # i += 1
            # if (i >= len (input)): return False
            # while (input[i] != '"'):
            #     i += 1
            #     if (i == len(input) - 1): return True
            #     if (i >= len (input)): return False

        elif (x is '(' or x is '[' or x is '{'):
            list.append (x)
        elif (x is ')' or x is ']' or x is '}' or x is '>'):
            if (len (list) >= 1):
                if (dict[x] == list[-1]):
                    list.pop ()
                else:
                    return False
            else:
                return False

        i += 1

    if (len (list) == 0):
        return True
    else:
        return False


# print(is_balanced('()'))
# print(is_balanced('([)]'))
# print(is_balanced('('))
# print(is_balanced('(abc)'))
# print(is_balanced('"("'))
# print(is_balanced("'abc'"))

print(is_balanced("()[abcd](<>)"))