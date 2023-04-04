def number_of_characters(string):
    """In this function we calculate he number of occurances for each letter of given string
    """
    dictionary = {i : string.count(string) for i in string}
    return dictionary
    
def main():
    enter = input()
    print(number_of_characters(enter))
main()