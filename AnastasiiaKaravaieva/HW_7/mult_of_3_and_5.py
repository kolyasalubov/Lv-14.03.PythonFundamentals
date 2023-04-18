def solution(number):
    sum = 0
    both_mult = []
    if number < 0:
        return 0
    else:
        for d in range(0, number):
            if d in both_mult:
                countinue
            elif d%3 == 0 and d%5 == 0:
                sum = sum + d
                both_mult.append(d)
            elif d%3 == 0 or d%5 == 0:
                sum = sum + d
            
    return sum