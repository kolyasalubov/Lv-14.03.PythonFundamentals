def count_sheeps(sheep):
    count = 0
    for el in sheep:
        if el == True:
            count = count + 1
        else:
            continue
    return count