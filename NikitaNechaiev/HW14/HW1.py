FILENAME = 'somefile.txt'
with open(FILENAME,'w',encoding='utf-8') as f:
    f.write('Hello SoftServe\n')
    f.write('---------\n')
with open(FILENAME,'a',encoding='utf-8') as f:
    f.write('Hello Python!!!\n')
    f.write('---------\n')

print('Reading message....')

with open(FILENAME,'r',encoding='utf-8') as f:
    for message in f:
        print(message)