def mergeIntervals(intervals):
    res = []
    intervals.sort()
    res.append(intervals[0])

    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res



intervals = [[1, 3],
             [2, 6],
             [8, 10],
             [15, 18]]

# intervals = [[1,4],[4,5]]
print(mergeIntervals(intervals))
