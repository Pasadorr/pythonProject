keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def generate_password(n):
    pairs = []
    n = int(n)
    for i in range(1, 21):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                pairs += str(i) + str(j)
    return pairs
for result in range(1, 21):
    result = int(input('Введите цифру от 3 до 20 включительно: '))
    if result < 3 or result > 20:
        print('Ты совершил ошибку, попробуй заново')
        continue
    if 1 <= result <= 20:
        print(f'[{result}] — [{generate_password(result)}]')
generate_password()
