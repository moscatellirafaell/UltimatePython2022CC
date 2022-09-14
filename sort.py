# list1 = [4, 1, 5, 3, 2]
# list2 = [('b', 10), ('a', 5), ('c', 3)]
#
# print(sorted(list1, reverse=True))
# print(sorted(list2, key=lambda item: item[1]))

fruits_li = ['banana', 'apple', 'melon', 'grape', 'strawberry']
fruits_qtd = [10, 23, 5, 33, 17]
comb_li = list(zip(fruits_li, fruits_qtd))

print(sorted(comb_li, key=lambda num: num[1]))
print(sorted(comb_li, key=lambda name: len(name[0])))
