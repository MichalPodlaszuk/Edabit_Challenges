def id_mtrx(n):
    try:
        return [[1 if i == abs((n + 1 - abs(n + 1))/2) + (abs(n)/n)*j else 0 for i in range(abs(n))] for j in range(abs(n))]
    except TypeError:
        return "Error"
    # abs((n + 1 - abs(n + 1))/2) = 0 for n positive, abs(n)-1 for n negative

print(id_mtrx(-20.0))
