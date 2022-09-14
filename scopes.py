multiplier = 2
has_calculated = False
print(has_calculated)


def multiply_calculator(arg):
    global has_calculated
    result = arg * multiplier
    has_calculated = True
    return result


print(multiply_calculator(6))
print(has_calculated)
