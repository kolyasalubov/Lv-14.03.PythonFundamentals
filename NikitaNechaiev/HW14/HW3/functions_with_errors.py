def greeting_by_name(name):
    return f"Hello {name}!"


def get_symbol_position(text, symbol):
    return text.find(symbol)
# print(get_symbol_position('Hello john!','l'))

def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1
# print(merge({'one , two'},{'three'}))
    