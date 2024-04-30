def check_winner():
    if area[0][0] == 'X' and area[0][1] and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] and area[2][0] == 'X':
        return 'X'
    if area[0][0] == '0' and area[0][1] and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][0] and area[2][0] == '0':
        return '0'
    if area[0][1] == '0' and area[1][1] and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] and area[2][2] == '0':
        return '0'
    if area[0][2] == '0' and area[1][1] and area[2][0] == '0':
        return '0'
    return '*'


def draw_area():
    for item in area:
        print(*item)
    print()

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
draw_area()

for turn in range(1, 10):
    print(f'Ваш ход {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')

    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки (1, 2, 3) ')) - 1
    column = int(input('Введите номер колонны (1, 2, 3) ')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Ты охуел?')
        draw_area()
        continue
    draw_area()

    if check_winner() == 'X':
        print('X won')
        break
    if check_winner() == '0':
        print('Zero won')
        break
    if check_winner() == '*' and turn_char == 9:
        print('Losers')
        break







