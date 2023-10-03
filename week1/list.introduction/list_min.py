ls = [58.4, 8, 9, 45, -8.1, 0, 16]

min = ls[0]
if all(isinstance(i, int) | isinstance(i, float) for i in ls):
    for i in range(len(ls)):
          if ls[i] < min:
            min = ls[i]
    print(min)
else: print("The list contains other types of elements than integer or float.")
