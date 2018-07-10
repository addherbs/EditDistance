def judgeCircle(moves):
    moves = str (moves)
    lastUnit = [0, 0]

    for i, unit in enumerate (moves):
        if (unit == 'U'):
            lastUnit[1] += 1
        elif (unit == 'D'):
            lastUnit[1] -= 1
        elif (unit == 'L'):
            lastUnit[0] -= 1
        elif (unit == 'R'):
            lastUnit[0] += 1
        if (lastUnit == [0, 0] and i == len (moves) - 1):
            return True

    return False

print (judgeCircle("UDLRR"))