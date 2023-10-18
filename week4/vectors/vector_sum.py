def vector_sum(n):
    V1 = [int(input("Enter coordinates of the first vector: ")) for i in range(n)]
    V2 = [int(input("Enter coordinates of the second vector: ")) for i in range(n)]
    return [V1[i] + V2[i] for i in range(n)]

print(vector_sum(3))
