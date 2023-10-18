def herons_formula(a,b,c):
    p = (a + b + c) / 2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    return area


#print(herons_formula(23, 41, 46))
