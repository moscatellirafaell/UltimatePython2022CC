# file = open('file1.txt')
# print(list(file))
# file.close()

# with open('file1.txt') as file1:
#     # print(file.read())
#     for line in list(file):
#         print(line)
#
# with open('file1.txt', 'a') as file1:
#     file.write('\nWrite some more text')

with open('file2.txt', 'w') as file2:
    file2.write('''
           *
          ***
         *****
        *******
           *
           *''')
