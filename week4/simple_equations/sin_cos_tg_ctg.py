def sin_cos_tg_ctg(a, b, c):
    cosx = (a**2 + b**2 -c**2) / (2*a*b)
    sinx = (1 - cosx**2) ** 0.5
    tgx = sinx/cosx if cosx != 0 else "Not defined"
    ctgx = cosx/sinx if sinx != 0 else "Not defined"
    return sinx, cosx, tgx, ctgx


print(sin_cos_tg_ctg(10, 24, 26))
print(sin_cos_tg_ctg(9, 5, 5))
print(sin_cos_tg_ctg(26, 24, 10))


