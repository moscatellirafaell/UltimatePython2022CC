# print(eval('5 + 10'))
# print(eval('"test".upper()'))
# exec('if True: print("true")')
# exec('a = 2')
# print(a)

# my_string = 'test'
# print(my_string.upper())
# print(my_string.title())
# print(my_string.lower())
# print(my_string.casefold())
for m in ['.upper()', '.title()', '.lower()', '.casefold()']:
    print(eval(f'"test"{m}'))
