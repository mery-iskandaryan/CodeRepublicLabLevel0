import scalar_product
import vector_norm


def angle_cosine(n):
    V1 = [int(input("Enter coordinates of the first vector: ")) for i in range(n)]
    V2 = [int(input("Enter coordinates of the second vector: ")) for i in range(n)]
    sp = scalar_product.scalar_product(n, V1, V2)
    V1_norm = vector_norm.vector_norm(V1)
    V2_norm = vector_norm.vector_norm(V2)
    return sp / (V1_norm * V2_norm)


print(angle_cosine(2))
