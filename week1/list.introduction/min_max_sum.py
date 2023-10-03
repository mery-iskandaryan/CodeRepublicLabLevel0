ls = [8,9,76,4,0,-16,32,66]

max = ls[0]
min = ls[0]
for i in range(len(ls)):
    if ls[i] > max:
        max = ls[i]

for i in range(len(ls)):
      if ls[i] < min:
        min = ls[i]

print(min+max)
