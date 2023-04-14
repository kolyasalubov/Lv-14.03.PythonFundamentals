def filter_words(st):
    new_string = [""]
    lowering_uppering_string = st[0].upper() + st[1:].lower()
    for i in lowering_uppering_string:
        if new_string[-1] != " " or i != " ":
            new_string.append(i)
    if new_string[-1] == " ":
        new_string = new_string[:-1]
    return "".join(new_string)