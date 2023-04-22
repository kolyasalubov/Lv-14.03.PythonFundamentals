def calc_char(string):
    result = {}
    for i in string:
        if i in result:  
            continue
        else:
            result.update({str(i):string.count(i)})
    return result

print(calc_char("Hello"))