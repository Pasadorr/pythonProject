
def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)
print_params()

def print_params(a = 1, b = 'String', c = True):
    if c is True:
        c = ['String']
        c.append('String 2x')
    print(a, b, c)

print_params()
print_params(a = 34, b = 2, c = False)
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params()


def print_params(a = 23, b = 'Like', c = False):
    print(a, b, c)
print_params()

values_list = [2, 'Bye', 2.3]
values_dict = {'a' : 'Body', 'b' : 21, 'c' : 'Kill'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2.1, 'Проверяем разные типы']
print_params(*values_list_2)
