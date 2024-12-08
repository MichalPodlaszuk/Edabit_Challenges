seats = [[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]


def can_see_stage(seats):
    for i in range(len(seats)-1):
        if not any([True if (seats[i+1][j] - seats[i][j]) > 0 else False for j in range(len(seats[i]))]):
            return False
        else:
            pass
    return True


print(can_see_stage(seats))