def test(*args):
    print(args)
print(test('Text,', 1, 2.21, False, [1, 22]))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print('Факториал числа 5 равен', factorial(5))
