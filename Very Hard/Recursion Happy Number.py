def is_happy(n):
    k = 0
    for i in str(n):
        k += int(i)**2
    if k == 1:
        return True
    elif k == 4:
        return False
    else:
        return is_happy(k)


print(is_happy(4))