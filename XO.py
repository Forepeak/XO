a, b, c, d, e, f, g, h, i = 1, 2, 3, 4, 5, 6, 7, 8, 9
number = False
rot = 1
numbers = []

import time

while True:

    if rot % 2 == 0:
        player = "o"
    else:
        player = "x"

    print(f'''
    {a} {b} {c}
    {d} {e} {f}
    {g} {h} {i}
    ''')

    while True:

        try:
            number = int(input(f"Выберите ячейку для вставки {player}  "))
        except Exception:
            print("Требуется ввести целое число в диапазоне 1-9")

        finally:
            if number <= 9 and not (str(number) in numbers):
                break
            else:
                print("Выберите пожалуйста пустую ячейку в диапазоне 1-9 ")

    if number == 1:
        a = player
    elif number == 2:
        b = player
    elif number == 3:
        c = player
    elif number == 4:
        d = player
    elif number == 5:
        e = player
    elif number == 6:
        f = player
    elif number == 7:
        g = player
    elif number == 8:
        h = player
    elif number == 9:
        i = player

    numbers += str(number)

    if a == player and b == player and c == player:
        print(f"{player} - выиграл !!!")
        print(f'''
           [{a}] [{b}] [{c}]
            {d}   {e}   {f}
            {g}   {h}   {i}
            Конец игры!''')
        time.sleep(5)
        break
    elif d == player and e == player and f == player:
        print(f"{player} - выиграл !!!")
        print(f'''
            {a}   {b}   {c}
           [{d}] [{e}] [{f}]
            {g}   {h}   {i}
            Конец игры!''')
        time.sleep(5)
        break
    elif g == player and h == player and i == player:
        print(f"{player} - выиграл !!!")
        print(f'''
            {a}   {b}   {c}
            {d}   {e}   {f}
           [{g}] [{h}] [{i}]
            Конец игры!''')
        time.sleep(5)
        break
    elif a == player and d == player and g == player:
        print(f"{player} - выиграл !!!")
        print(f'''
           [{a}] {b} {c}
           [{d}] {e} {f}
           [{g}] {h} {i}
           Конец игры!''')
        time.sleep(5)
        break
    elif b == player and e == player and h == player:
        print(f"{player} - выиграл !!!")
        print(f'''
           {a} [{b}] {c}
           {d} [{e}] {f}
           {g} [{h}] {i}
            Конец игры!''')
        time.sleep(5)
        break
    elif c == player and f == player and i == player:
        print(f"{player} - выиграл !!!")
        print(f'''
           {a} {b} [{c}]
           {d} {e} [{f}]
           {g} {h} [{i}]
            Конец игры!''')
        time.sleep(5)
        break
    elif a == player and e == player and i == player:
        print(f"{player} - выиграл !!!")
        print(f'''
           [{a}] {b}  {c}
            {d} [{e}] {f}
            {g}  {h} [{i}]
           Конец игры!''')
        time.sleep(5)
        break
    elif g == player and e == player and c == player:
        print(f"{player} - выиграл !!!")
        print(f'''
           {a}   {b} [{c}]
           {d}  [{e}] {f}
           [{g}] {h}  {i}
            Конец игры!''')
        time.sleep(5)
        break
    rot += 1
