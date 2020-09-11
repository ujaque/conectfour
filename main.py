
# columns, lines = 4, 3
# Matrix = [['*' for x in range(columns)] for y in range(lines)]

# print(Matrix)


def boardisfull(tablero):
    boardfull = True
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == '*':
                boardfull = False

    return boardfull


def createboard(rows, columns):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append('*')
        board.append(row)
    return board


def createboard2(rows, columns):
    board = [['*' for x in range(columns)] for x in range(rows)]
    return board


def printboard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()

    for i in range(len(board[0])):
        print(i, end=' ')
    print()


def playermove(player, move):

    if player == 1:
        symbol = 'X'
    else:
        symbol = '0'
    for i in range(len(matriz)):
        if matriz[-1-i][move] == '*':
            matriz[-1-i][move] = symbol
            break


def columisfull(colum):
    isfull = True

    for i in range(len(matriz)):
        if matriz[i][colum] == '*':
            isfull = False
            break
    return isfull


def game():

    player = 1
    printboard(matriz)
    while not boardisfull(matriz):

        try:
            move = int(input(f'Insert player {str(player)} move: '))
            if not columisfull(move):

                playermove(player, move)
                print('\n')
                printboard(matriz)
                if player == 1:
                    player = 2
                else:
                    player = 1
            else:
                print('column is full')
        except:
            print('Introduce a valid character')
    else:
        print('tie game')


matriz = createboard2(3, 3)
game()
