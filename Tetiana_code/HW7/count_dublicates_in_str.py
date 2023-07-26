# write a function that calculates the number of characters included in 
# given string input: "hello"  
# output: {"h": 1, "e":1, "l": 2, "o": 1 }

def count_characters(str):
    new_char = {}
    for char in str:
        if char in new_char:
            new_char[char] += 1
        else:
            new_char[char] = 1
    return new_char


str = "hello"
result = count_characters(str)
print(result)