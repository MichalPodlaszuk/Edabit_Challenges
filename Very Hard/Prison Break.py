cells = [1, 1, 1]


def freed_prisoners(arr):
    if arr[0] == 0:
        return 0
    else:
        freed = 1
        while 0 in arr:
            arr = arr[arr.index(0):]
            arr = [1 if i==0 else 0 for i in arr]
            freed += 1
        return freed


print(freed_prisoners(cells))

