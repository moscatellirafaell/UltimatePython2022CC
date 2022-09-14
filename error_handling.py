# anticipating errors/ exceptions
# try:
#     print('try')
#     print(a)
#     print(1/0)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except NameError:
#     print('Does not exist')
# else:
#     print('The else statement')
# finally:
#     print('Finally')

# raising exceptions
# var_must_be_string = []
# if isinstance(var_must_be_string, str):
#     print(var_must_be_string)
# else:
#     raise TypeError('Must be a string')

# assert
# a = 5
# assert a == 6

# exercise
test_list = [1, 2, 3]
try:
    print(test_list[3])
except IndexError:
    print('Index does not exist')
else:
    print('else')
finally:
    print('finally')
