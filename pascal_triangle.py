def pascal(numRows):
    triangle = []
    for i in range(1, numRows+1):
        row = [1] * i
        triangle.append(row)

    for j in range(2, len(triangle)):
        for k in range(1, len(triangle[j]) - 1):
            triangle[j][k] = triangle[j-1][k-1] + triangle[j-1][k]
    return triangle





print(pascal(5))
