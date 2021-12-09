def new_board():
    return [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]


def print_board(board):
    print("╭───────╮")
    for row in board:
        print("│ ", end='')
        for val in row:
            print(val + ' ', end='')
        print('│')
    print("╰───────╯")


def pad_screen():
    i = 0;
    while i < 100:
        print();
        i += 1


def main():
    board = new_board()
    turn(board)


def turn(board):
    # TODO True will be replaced with a function that checks for a winner, which will break the loop.
    is_player1 = True
    while True:
        pad_screen()
        print_board(board)
        while True:
            try:
                # get input and convert it into a row/column numbers
                print("[", "X" if is_player1 else "O", "] Select your next move")
                loc = input("ROW COLUMN | ")
                vals = loc.replace(',', '').split(' ')
                row = int(vals[0])
                column = int(vals[1])

                if not 0 < row * column < 10:
                    raise ValueError

                if board[row-1][column-1] != '-':
                    print("----------------------------------------------------")
                    print("  That spot has already been used!")
                    print("  Please select a blank space!!")
                    print("----------------------------------------------------")
                    continue
                else:
                    board[row-1][column-1] = 'X' if is_player1 else 'O'
                    is_player1 = not is_player1
                    break

            except ValueError:
                print("====================================================")
                print("  I'm sorry, I didn't recognize your input!")
                print("  Please specify a number 1-3 for the ROW and COLUMN")
                print("====================================================")


main()


