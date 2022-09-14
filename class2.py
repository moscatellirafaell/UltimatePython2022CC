# def add(a, b):
#     return a + b
#
#
# class Test:
#     def __init__(self, add_function):
#         self.add_function = add_function
#
#
# test = Test(add)
# print(test.add_function(1, 2))


class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:
    def bite(self):
        print('bite')

    def strike(self):
        print('strike')

    def slash(self):
        print('slash')

    def kick(self):
        print('kick')


monster1 = Monster(Attacks().bite)
monster2 = Monster(Attacks().strike)

monster1.func()
monster2.func()
