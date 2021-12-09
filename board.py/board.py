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


def main():
    board = new_board()
    print_board(board)


main()


