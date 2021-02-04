def zad(n):
    w = 0
    while n != 0 and n != 1:        
        if n % 2 == 0:
            n = n // 4
        else:
            n = 3 * n + 1
        w += 1
    w += 1
    return(w)
print(zad(5))