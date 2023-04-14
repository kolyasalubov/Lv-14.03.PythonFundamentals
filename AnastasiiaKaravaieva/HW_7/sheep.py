def count_sheeps(sheep):
    counted_sheep = []
    for sh in sheep:
        if sh == True:
            counted_sheep.append(sh)
    return len(counted_sheep)