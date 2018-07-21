s = "2-4AOr7-4k"
k = 4

def check(s, k):
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

print (check(s,k ))


