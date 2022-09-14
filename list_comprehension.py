# list1 = [num for num in range(10)]
# list2 = [num if num % 2 == 0 else 'x' for num in range(10)]
# list3 = [[(x, y) for x in range(10)] for y in range(2)]
#
# print(list1)
# print(list2)
# print(list3)

chess = [[f'{let}{num}' for num in range(1, 9)] for let in 'ABCDEFGH'[::-1]]

for row in chess:
    print(row)
