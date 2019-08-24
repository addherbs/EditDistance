
import collections


def test(p, q):
    dict1 = collections.Counter(p)
    dict2 = collections.Counter(q)
    res = []
    for each in dict1:
        if each in dict2:
            temp = [each] * min(dict1[each], dict2[each])
            res.extend(temp)

    return res


p = [1, 1, 2, 3, 4, 5, 4]
q = [1, 1, 2, 3, 4, 5]
print(test(p, q))
