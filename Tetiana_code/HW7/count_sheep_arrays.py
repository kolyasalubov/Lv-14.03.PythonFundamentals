
def count_sheep(sheep_array):
    count = 0
    for sheep in sheep_array:
        if sheep == True:
            count += 1
    return count


sheep = [True, False, True, True, False, True]
sheep_count = count_sheep(sheep)
print(sheep_count)  
