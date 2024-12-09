def party_people(arr):
    for i in arr:
        if i > len(arr):
            arr.remove(i)
            return party_people(arr)
        else:
            pass
    return len(arr)


print(party_people([10, 12, 15, 15, 5]))