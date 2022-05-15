print("Tic Tac Toe")

matrix = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]
Round = 0
Turns = 9
Game = {'00': '   ', '01': '   ', '02': '   ',
        '10': '   ', '11': '   ', '12': '   ',
        '20': '   ', '21': '   ', '22': '   '}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(str(i), str(j), end="    ")
    print()
print()

while Turns > 0:
    if Turns % 2 == 0:
        sign = ' 0 '
        Player = 2
    else:
        sign = ' X '
        Player = 1

    Round += 1
    if Round == 9:
        print('Final Round')
    else:
        print('Round: ', Round)

    print('Player : ', Player)
    xy = input("Enter the position ")
    x, y = list(xy)

    if int(x) in [0, 1, 2] and int(y) in [0, 1, 2] and xy in Game.keys() and Game[xy] == '   ':
        print("Valid Input")

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if xy == (str(i) + str(j)):
                    print(sign, end='')
                else:
                    print(Game[str(i) + str(j)], end='')
            print()
        print()
    else:
        Round -= 1
        print(' Invalid Input, Try Again !!')
        continue
    Turns -= 1

    if Game['00'] == Game['01'] == Game['02'] == ' X ' or Game['10'] == Game['11'] == Game['12'] == ' X ' or Game[
        '20'] == Game['21'] == Game['22'] == ' X ' or Game['00'] == Game['10'] == Game['20'] == ' X ' or Game['01'] == \
            Game['11'] == Game['21'] == ' X ' or Game['02'] == Game['12'] == Game['22'] == ' X ' or Game['00'] == Game[
        '11'] == Game['22'] == ' X ' or Game['02'] == Game['11'] == Game['20'] == ' X ':
        print('Player ' + str(Player) + ' Won')
        break
    elif Game['00'] == Game['01'] == Game['02'] == ' O ' or Game['10'] == Game['11'] == Game['12'] == ' O ' or Game[
        '20'] == Game['21'] == Game['22'] == ' O ' or Game['00'] == Game['10'] == Game['20'] == ' O ' or Game['01'] == \
            Game['11'] == Game['21'] == ' O ' or Game['02'] == Game['12'] == Game['22'] == ' O ' or Game['00'] == Game[
        '11'] == Game['22'] == ' O ' or Game['02'] == Game['11'] == Game['20'] == ' O ':
        print('Player ' + str(Player) + ' Won')
        break

    Game[xy] = sign
    print()
