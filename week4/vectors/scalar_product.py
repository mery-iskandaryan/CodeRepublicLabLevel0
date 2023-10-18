def scalar_product(n, V1, V2):
    #V1 = [int(input("Enter coordinates of the first vector: ")) for i in range(n)]
    #V2 = [int(input("Enter coordinates of the second vector: ")) for i in range(n)]
    sc = [V1[i] * V2[i] for i in range(n)]
    sum = 0
    for i in sc:
        sum += i
    return sum


print(scalar_product(3, [1,2,3], [4,5,6]))
