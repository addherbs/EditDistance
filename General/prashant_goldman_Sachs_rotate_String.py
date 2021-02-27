def rotateTheString(originalString, direction, amount):
    print originalString, direction, amount
    for di, am in zip(direction, amount):
        print originalString
        am = am % len(originalString)
        if not di:
            originalString = originalString[am:] + originalString[:am]
        else:
            originalString = originalString[-am:] + originalString[:-am]

    return originalString


oS = "hurart"
di = [0, 1]
amount = [4, 1]

print rotateTheString(oS, di, amount)
