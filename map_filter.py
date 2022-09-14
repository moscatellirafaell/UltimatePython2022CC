list1 = [1, 2, 3, 4, 5]


# def pow_func(num):
#     return num ** 2


# def get_below_4(num):
#     if num < 4:
#         return True
#     else:
#         False


# print(list(map(lambda num: num ** 2, list1)))
# print(list(filter(lambda num: num < 4, list1)))

print(list([num ** 2 for num in list1]))
print(list([num for num in list1 if num < 4]))
