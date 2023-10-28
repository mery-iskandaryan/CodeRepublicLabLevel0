with open('matrix.txt', 'r') as mat:
    matrix = mat.read()
    matrix = matrix.splitlines()
for i in range(len(matrix)):
    matrix[i] = matrix[i].split(',')
m = [[131,673,234, 103, 18],
     [201,96,342, 965, 150],
     [630,803,746,422,111],
     [537, 699, 497, 121, 956],
     [805, 732, 524, 37, 331]]

dp = [[0 for i in range(80)] for j in range(80)]
dp[0][0] = matrix[0][0]
for i in range(1, 80):
    dp[0][i] = int(matrix[0][i]) + int(dp[0][i - 1])
for i in range(1, 80):
    dp[i][0] = int(matrix[i][0]) + int(dp[i - 1][0])
for i in range(1, 80):
    for j in range(1, 80):
        dp[i][j] = int(matrix[i][j]) + min(int(dp[i - 1][j]), (dp[i][j - 1]))
print(dp[-1][-1])
