
#HW3#HW3#HW#HW3#HW3#HW3#HW3#HW3#HW3


# def solve(string):
#     output = {}
#     string2 = string.lower()
#     for i in string2:
#         keys = output.keys()
#         if i not in keys:
#             output[i] = 1
#         else:
#             output[i] += 1
#     return output

# print(solve('google'))
# print(solve('Google'))











#Вирішив зробити таку штуку інтеркативну програмку



def word_counter():      #намудрив функцію с циклом  трохи але вона працює
    '''
    That functions
    takes string and
    gives you a variants
    to choose option:
    1.Count total length
    2.Count word symbols
    3.Close the program
    '''
    while True:
        sttr = input('Choose the option:\n 1.Close the program.\n 2.Enter a word\n')
        if sttr == '1':
             print("Program closed.")
             break
        elif sttr == '2':
             word = (input('Enter a word: '))
        print('Choose the option:\n 1.Total length\n 2.Count symbols\n')
        choice = input()
        if choice == '1' :
            print('The total length of the word | {} | is {} symbols.'.format(word,len(word)))
        elif choice == '2' :
            char = input('Enter a symbol: ')
            if char in word:
                print('That string contains symbol | {} | {} times. '.format(char,word.count(char)))
            else:
                print('Invalid option!')
        else:
                print('Invalid option!')
print(word_counter.__doc__)   
word_counter()
