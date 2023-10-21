def climbStairs(n):
    num1 = 0
    num2 = 1
    for _ in range(n):
        res = num1 + num2
        num1, num2 = num2, res
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
