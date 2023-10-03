ls = [1,5,-1,5,58,99,87,0,4,6,10]

max = ls[0]
if all(isinstance(i, int) | isinstance(i, float) for i in ls):
    for i in range(len(ls)):
          if ls[i] > max:
            max = ls[i]
    print(max)
else: print("The list contains other types of elements than integer or float.")
