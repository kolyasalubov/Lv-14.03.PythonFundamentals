def solution(number):
    result = 0
    set_of_result = {0}
    if number < 0:
        return 0
    elif number >= 0:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                set_of_result.add(i)
            else:
                continue
        for int in set_of_result:
            result = result + int

        return result