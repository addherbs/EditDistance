def get_min_number_flights(weights):
    if (not weights):
        return 0
    if (len (weights) < 3):
        return 1

    g = sorted(weights)
    x = []
    for each in g:
        if (each <= 150):
            x.append(each)

    weights = x
    print(weights)
    m = 150
    i = 0
    j = len (weights) - 1
    temp = []
    while (i < j):
        if (weights[i] + weights[j] <= m):
            temp.append ([weights[i], weights[j]])
            i += 1
            j -= 1
        else:
            temp.append ([weights[j]])
            j -= 1
        if (i == j):
            temp.append (weights[i])
            break

    return len (temp)


print(get_min_number_flights([6,50,80,120,100,50,160]))