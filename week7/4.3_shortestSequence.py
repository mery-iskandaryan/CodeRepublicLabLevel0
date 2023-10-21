def shortestSequence(rolls, k):
    res = 0
    roll = set(rolls)
    for i in rolls:
        roll.add(i)
        if len(roll) == k:
            res += 1
            roll.clear()
    return res + 1
