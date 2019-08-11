# Not fully completed with runtime

from collections import Counter


def threeSumMulti(A, target):
    n = len(A)
    A.sort()
    result = []

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if A[i] + A[j] + A[k] == target:
                    result.append((A[i], A[j], A[k]))
    print(result)
    return len(result)


print(threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
