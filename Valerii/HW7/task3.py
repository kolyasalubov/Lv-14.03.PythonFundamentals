def char_numbers(s: str) -> dict:
    """ The function calculates the number of characters included in giving string. Returns dictionary."""
    characters = []
    for char in s:
        if char not in characters:
            characters.append(char)
    numbers = {character:s.count(character) for character in characters}
    return numbers

