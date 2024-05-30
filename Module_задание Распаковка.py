def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)
print_params()
print_params(4)
print_params(4, 7)
print_params(None)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [34, 'Strope', False]
values_dict = {'a': 10, 'b': 'Strip', 'c': 2.5}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5903, 'Missile']
print_params(*values_list_2, 42)