def max_flourists(path_length, florist_intervals):


    length = 0
    min_first_index = florist_intervals[0][0]
    max_last_index = florist_intervals[0][1]
    for each in florist_intervals:
        if (min_first_index > each[0]): min_first_index = each[0]
        if (max_last_index < each[1]): max_last_index = each[1]

    # print (max_last_index +  path_length + 1)
    array = [0] * (max_last_index+ path_length + 1)
    for i,each in enumerate(florist_intervals):
        florist_intervals[i].insert(0, each[1] - each[0])

    florist_intervals.sort(reverse = True, key = lambda x: x[0])
    # print ()

    for each in florist_intervals:
        temp_low = each[1]
        temp_high = each[2]
        if (temp_low >= min_first_index and temp_low < min_first_index+path_length and min(array[temp_low:temp_high+1]) < 3 ):
            for i in range (temp_low, temp_high +1):
                if (i < len(array) ): array[i] += 1
            length += 1

    print(florist_intervals, array, len(array))
    return length

print(max_flourists(9, [[1,10],[1,6], [2,8], [3,5]]))
print("============================================")
print(max_flourists(5, [[0,1],[1,2], [2,3], [3,4], [4,5]]))
print("============================================")
print(max_flourists(6, [[0,1],[0,1],[0,1],[1,2], [1,2], [1,2]]))
print("============================================")
print(max_flourists(5, [[0,5],[0,5],[0,5],[0,5],[0,5],[5,6], [6,7]]))