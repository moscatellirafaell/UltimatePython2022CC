import string
from math import floor as get_floor
from random import *
from datetime import datetime

random_number = randint(0, 10)
print(random_number)

test_list = ['hi', 'hello', True, [1, 2, 3]]
print(choice(test_list))

print(string.ascii_lowercase)

print(get_floor(14.9))

print(datetime.now())
