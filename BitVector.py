import numpy as np


class BitVector:
    def __init__(self, vector_size: int) -> None:
        self.array_size = (vector_size // 64) + 1  # v_size = 66 a_size = 2
        self.array = np.zeros(self.array_size, dtype="uint64") # [00000000 ,  00000000]

    def setBit(self, index):
        array_index = index // 64  # 9
        self.array[self.array.size - array_index - 1] |= np.uint64(1 << index % 64)

    def resetBit(self, index):
        array_index = index // 64
        self.array[self.array_size - array_index - 1] &= ~np.uint64(1 << index % 64)

    def getBit(self, index):
        array_index = index // 64
        return self.array[self.array.size - array_index - 1]


bit_vector = BitVector(200)
bit_vector.setBit(64)
bit_vector.setBit(65)

