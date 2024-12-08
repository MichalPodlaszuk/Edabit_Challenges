def snakefill(n):
    i = 1
    j = 0
    while 2*i < n**2:
        i *= 2
        j += 1
        print(i, j)
    return j


print(snakefill(3))