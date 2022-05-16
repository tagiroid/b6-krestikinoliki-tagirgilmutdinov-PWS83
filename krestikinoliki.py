field = list('123456789')

def board():
    for i in range(3):
        print('.... ... ....')
        print(':', field[i * 3 + 0], ':', field[i * 3 + 1], ':', field[i * 3 + 2], ':')
    print('.... ... ....')


def player(sign):
    while True:
        your_turn = input('Ходит ' + sign + ': ')
        if not (your_turn in '1 2 3 4 5 6 7 8 9'):
            print('Нет такого хода')
            continue
        your_turn = int(your_turn)
        if str(field[your_turn - 1]) in 'x0':
            print('Уже занято')
            continue
        field[your_turn - 1] = sign
        break


win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]


def winner():
    for i in win:
        if (field[i[0]-1]) == (field[i[1]-1]) == (field[i[2]-1]):
            return (field[i[0]-1])
    else:
        return False

def game():
    turn = 0
    while True:
        board()
        if turn % 2 == 0:
            player('x')
        else:
            player('0')
        if turn > 3:
            win = winner()
            if win:
                board()
                print(win, "побеждают")
                break
        turn += 1
        if turn > 8:
            board()
            print('Никто не победил')
            break


game()
