def multiply_by_number(n, k):
    V = []
    for i in range(n):
        V.append(int(input("Enter the coordinates: ")))
    V_k = []
    for i in range(len(V)):
        V_k.append(V[i] * k)
    return V_k


print(multiply_by_number(2, 10))
