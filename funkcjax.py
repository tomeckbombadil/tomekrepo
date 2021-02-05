from math import sqrt


def zad(x):
    w = 0
    if x < 7:
        w = x ** 3 + 1
    elif x == 7:
        w = x - 1
    elif x == 9:
        w = sqrt(3 * x)
    else:
        w = - 8 * x
    return(w)
print(zad(295))