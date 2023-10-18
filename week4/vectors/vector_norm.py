def vector_norm(vector):
    norm = [i ** 2 for i in vector]
    sum = 0
    for i in norm:
        sum += i
    return sum ** 0.5


#print(vector_norm([3,4]))
