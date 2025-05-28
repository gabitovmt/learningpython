import random
import time


def dice():
    player = random.randint(1, 6)
    print('У тебя выпало ' + str(player))
    print('Компьютер делает бросок ...')
    time.sleep(2)

    ai = random.randint(1, 6)
    print('У компьютера выпало ' + str(ai))

    if player > ai:
        print('Ты победил')
    elif player < ai:
        print('Ты проиграл')
    else:
        print('Ничья')

    while True:
        print('Выход? y/n')
        is_continue = input()

        if is_continue.lower() == 'y':
            exit()
        elif is_continue.lower() == 'n':
            break
        else:
            print('Твой выбор непонятен. Сыграешь ещё раз?')


while True:
    print('Нажми кнопку ввода, чтобы бросить кубик')
    roll = input()
    dice()
