def trapezoid_area(AB, AH, AD):
    CD = AB
    BH = (AB**2 - AH**2)**0.5
    BC = AD - (2*AH)
    area = ((BC + AD) / 2) * BH
    res = "BC = {}, area = {}".format(BC, area)
    return res


#print(trapezoid_area(8, 4, 16))
#print(trapezoid_area(25, 7, 30))


